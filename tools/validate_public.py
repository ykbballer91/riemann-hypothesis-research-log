#!/usr/bin/env python3
"""Validate the publication payload, links, state, manifest, and deployment gate.

Copyright (c) 2026 @ykbballer91. SPDX-License-Identifier: MIT
This is publication validation, not verification of mathematical theorems.
"""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml
from build_site import ROOT, public_files, render_markdown


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "a" and values.get("name"):
            self.ids.add(values["name"])
        for name in ("href", "src"):
            if values.get(name):
                self.links.append(values[name])


def parse_document(path):
    text = path.read_text(encoding="utf-8")
    parsed = Links()
    parsed.feed(render_markdown(text) if path.suffix == ".md" else text)
    return parsed


def check_links(files, base, errors):
    docs = {p: parse_document(p) for p in files if p.suffix in (".md", ".html")}
    count = 0
    for source, parsed in docs.items():
        for target in parsed.links:
            parts = urlsplit(target)
            if parts.scheme or target.startswith("//"):
                continue
            count += 1
            decoded = unquote(parts.path)
            path = ((base / decoded.lstrip("/")) if decoded.startswith("/") else source.parent / decoded).resolve() if decoded else source
            if not path.is_relative_to(base):
                errors.append({"file":str(source.relative_to(base)), "type":"link_escapes_public_root", "target":target})
                continue
            if not path.exists():
                errors.append({"file":str(source.relative_to(base)), "type":"missing_link_target", "target":target})
            elif parts.fragment and path in docs and unquote(parts.fragment) not in docs[path].ids:
                errors.append({"file":str(source.relative_to(base)), "type":"missing_anchor", "target":target})
    return count


def validate(site=False):
    errors = []
    files = list(public_files())
    count = check_links(files, ROOT, errors)
    for source in files:
        if source.suffix == ".json":
            try:
                json.loads(source.read_text())
            except (ValueError, UnicodeDecodeError):
                errors.append({"file":str(source.relative_to(ROOT)), "type":"invalid_json"})
    for p in ("README.md", "docs/index.md", "docs/current-state.md"):
        if "**STATUS: RIEMANN HYPOTHESIS OPEN**" not in (ROOT/p).read_text():
            errors.append({"file":p, "type":"missing_OPEN_banner"})
    citation = yaml.safe_load((ROOT / "CITATION.cff").read_text())
    if citation.get("authors") != [{"name":"@ykbballer91", "website":"https://github.com/ykbballer91"}]:
        errors.append({"file":"CITATION.cff", "type":"creator_attribution_mismatch"})
    if citation.get("date-released"):
        errors.append({"file":"CITATION.cff", "type":"premature_public_release_date"})
    state = json.loads((ROOT / "data/research-state.json").read_text())
    if state.get("rh_status") != "OPEN" or state.get("rh_closed") is not False:
        errors.append({"file":"data/research-state.json", "type":"RH_status_mismatch"})
    manifest = json.loads((ROOT / "data/source-manifest.json").read_text())
    records = manifest if isinstance(manifest, list) else manifest.get("sources", manifest.get("records", manifest.get("entries", [])))
    if not records:
        errors.append({"file":"data/source-manifest.json", "type":"empty_or_unknown_manifest_schema"})
    for record in records:
        destination = record.get("public_destination", record.get("destination", record.get("public_path")))
        expected = record.get("export_sha256", record.get("public_sha256"))
        if not destination or not expected:
            errors.append({"file":"data/source-manifest.json", "type":"missing_export_provenance_fields", "source":record.get("source_path")})
        elif not (ROOT/destination).is_file() or hashlib.sha256((ROOT/destination).read_bytes()).hexdigest() != expected:
            errors.append({"file":destination, "type":"export_hash_mismatch"})
    workflow = yaml.load((ROOT/".github/workflows/pages.yml").read_text(), Loader=yaml.BaseLoader)
    condition = workflow["jobs"]["deploy"]["if"]
    if not all(s in condition for s in ("workflow_dispatch", "inputs.deploy == true", "repository.private == false", "PUBLICATION_APPROVED")):
        errors.append({"file":".github/workflows/pages.yml", "type":"deployment_gate_missing"})
    site_count = 0
    if site:
        build = ROOT / "_site"
        site_files = [p for p in build.rglob("*") if p.is_file()]
        site_count = check_links(site_files, build, errors)
        if not (build/"index.html").is_file() or "STATUS: RIEMANN HYPOTHESIS OPEN" not in (build/"index.html").read_text():
            errors.append({"file":"_site/index.html", "type":"site_OPEN_banner_missing"})
        for p in site_files:
            if p.suffix == ".html" and re.search(r"MATHPLACEHOLDER\d+END",p.read_text()):
                errors.append({"file":str(p.relative_to(ROOT)),"type":"unexpanded_math_placeholder"})
    return {"status":"FAIL" if errors else "PASS", "scope":"Publication files and local link/build consistency; no external URL crawl or mathematical proof check", "public_files":len(files), "source_records":len(records), "markdown_local_links_checked":count, "site_local_links_checked":site_count, "errors":errors}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = validate(args.site)
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output)
    print(output)
    sys.exit(result["status"] != "PASS")
