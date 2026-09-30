#!/usr/bin/env python3
"""Build a small, portable Markdown research site; no deployment is performed.

Copyright (c) 2026 @ykbballer91. SPDX-License-Identifier: MIT
"""
from __future__ import annotations

import argparse
import html
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import quote, unquote, urlsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_AUDITS = {
    "rewrite_manifest.md", "phase2_safety_report.md",
    "phase2_independent_review.md", "phase2_publication_review.md",
    "phase2_validation_summary.json",
}
ROOT_FILES = {
    "README.md", "LICENSE-TEXT", "LICENSE-CODE", "CITATION.cff",
    "requirements-site.txt",
}


def public_files():
    for name in sorted(ROOT_FILES):
        p = ROOT / name
        if p.is_file():
            yield p
    for dirname in ("docs", "archive", "artifacts", "data", "assets", "tools"):
        for p in sorted((ROOT / dirname).rglob("*")):
            if p.is_file() and not p.is_symlink() and "__pycache__" not in p.parts:
                yield p
    for name in sorted(PUBLIC_AUDITS):
        p = ROOT / "audit" / name
        if p.is_file():
            yield p


def protect_math(text):
    """Keep TeX out of Markdown's backslash/emphasis parser, including archives."""
    pieces = re.split(r"(```[\s\S]*?```|~~~[\s\S]*?~~~|`[^`\n]+`)", text)
    formulas = []
    pattern = re.compile(r"\$\$([\s\S]*?)\$\$|\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)|(?<!\\)\$([^$\n]+?)(?<!\\)\$")

    def substitute(match):
        block = match.group(1) is not None or match.group(2) is not None
        formula = next(g for g in match.groups() if g is not None)
        tag = "div" if block else "span"
        delimiters = (r"\[", r"\]") if block else (r"\(", r"\)")
        token = f"MATHPLACEHOLDER{len(formulas):07d}END"
        formulas.append(f'<{tag} class="math-{ "display" if block else "inline" }">'
                        + delimiters[0] + html.escape(formula) + delimiters[1] + f'</{tag}>')
        return "\n\n" + token + "\n\n" if block else token

    for i in range(0, len(pieces), 2):
        pieces[i] = pattern.sub(substitute, pieces[i])
    return "".join(pieces), formulas


def render_markdown(text):
    protected, formulas = protect_math(text)
    body = markdown.markdown(protected, extensions=["extra", "toc", "sane_lists"])
    for i, value in enumerate(formulas):
        token = f"MATHPLACEHOLDER{i:07d}END"
        body = body.replace(f"<p>{token}</p>", value).replace(token, value)
    return body


def site_path(path):
    return path.with_suffix(".html") if path.suffix.lower() == ".md" else path


def rewrite_links(body, source, destination, existing):
    def fix(match):
        attr, original = match.group(1), html.unescape(match.group(2))
        parsed = urlsplit(original)
        if parsed.scheme or original.startswith(("//", "#")):
            return match.group(0)
        if not parsed.path:
            return match.group(0)
        decoded = unquote(parsed.path)
        target = (ROOT / decoded.lstrip("/") if decoded.startswith("/")
                  else source.parent / decoded).resolve()
        try:
            relative = target.relative_to(ROOT)
        except ValueError:
            return match.group(0)
        mapped = site_path(relative) if target in existing else relative
        rel = os.path.relpath(mapped, destination.parent)
        value = quote(rel, safe="/-_.~")
        if parsed.query:
            value += "?" + parsed.query
        if parsed.fragment:
            value += "#" + parsed.fragment
        return f'{attr}="{html.escape(value, quote=True)}"'
    return re.sub(r'(href|src)="([^"]*)"', fix, body)


def page(body, title, destination):
    def link(p):
        return quote(os.path.relpath(p, destination.parent), safe="/-_.~")
    nav = [
        ("Guide", "docs/index.html"), ("Current state", "docs/current-state.html"),
        ("Timeline", "docs/timeline.html"), ("Roadmap", "docs/roadmap.html"),
        ("Sources", "docs/source-map.html"),
    ]
    links = "".join(f'<a href="{link(p)}">{label}</a>' for label, p in nav)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · RH Research Log</title>
<meta name="description" content="AI-assisted research log. Riemann Hypothesis OPEN. Auxiliary results, failed routes, and unresolved gaps.">
<link rel="stylesheet" href="{link('assets/site.css')}">
<script>window.MathJax={{tex:{{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']],tags:'ams'}},options:{{skipHtmlTags:['script','noscript','style','textarea','pre','code']}}}};</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js"></script>
</head><body>
<a class="skip" href="#content">Skip to content</a>
<header><a class="brand" href="{link('index.html')}">RH <span>Research Log</span></a><nav aria-label="Main navigation">{links}</nav></header>
<div class="status-band"><strong>STATUS: RIEMANN HYPOTHESIS OPEN</strong><span>Publication-review draft · v0.1.0</span></div>
<main id="content">{body}</main>
<footer><span>@ykbballer91 · AI-assisted research</span><a href="{link('docs/methodology.html')}">Evidence &amp; method</a><a href="{link('docs/licensing.html')}">CC BY 4.0 text / MIT code</a></footer>
</body></html>'''


def build(output):
    output = output.resolve()
    if output != ROOT / "_site":
        raise SystemExit("The build output is restricted to this repository's _site directory.")
    if output.exists():
        shutil.rmtree(output)
    output.mkdir()
    sources = list(public_files())
    existing = set(sources)
    rendered = 0
    for source in sources:
        relative = source.relative_to(ROOT)
        destination = site_path(relative)
        target = output / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix.lower() != ".md":
            shutil.copyfile(source, target)
            continue
        text = source.read_text(encoding="utf-8")
        title_match = re.search(r"^#\s+(.+)", text, re.M)
        title = title_match.group(1).strip() if title_match else source.stem
        body = rewrite_links(render_markdown(text), source, destination, existing)
        target.write_text(page(body, title, destination), encoding="utf-8")
        rendered += 1
        if relative.as_posix() == "docs/index.md":
            home = Path("index.html")
            homebody = rewrite_links(render_markdown(text), source, home, existing)
            (output / home).write_text(page(homebody, title, home), encoding="utf-8")
    (output / ".nojekyll").write_text("")
    print(json.dumps({"rendered_markdown_pages": rendered, "copied_or_rendered_public_files": len(sources), "output": "_site", "deployment_performed": False}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    build(args.output)

