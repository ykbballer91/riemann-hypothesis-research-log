#!/usr/bin/env python3
"""Build a small, portable Markdown research site; no deployment is performed.

Copyright (c) 2026 @ykbballer91. SPDX-License-Identifier: MIT
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import quote, unquote, urlsplit

import markdown
from site_routes import SITE_URL, LANGUAGES, NAV, editorial_info, legacy_info, route, source_for, url_for

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_AUDITS = {
    "l7_publication_review.md",
    "cycles_6_17_publication_review.md",
    "handoff_2026_10_05_review.md",
    "bilingual_review.md", "bilingual_inventory.json", "bilingual_validation.json",
    "rewrite_manifest.md", "phase2_safety_report.md",
    "phase2_independent_review.md", "phase2_publication_review.md",
    "phase2_validation_summary.json",
    "phase3_final_content_review.md", "phase3_independent_review.md",
    "phase3_citation_review.md", "phase3_citation_inventory.json", "phase3_track_discrepancies.md",
    "phase3_traceability.md", "phase3_claims_inventory.json",
    "phase3_validation_summary.json", "phase3_safety_report.md",
    "phase3_content_changes.md", "publication_report.md",
}
ROOT_FILES = {
    "README.md", "README.ja.md", "LICENSE-TEXT", "LICENSE-CODE", "CITATION.cff",
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
    info = editorial_info(path)
    if info:
        return route(*info)
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


def legacy_anchors(body, key):
    """Retain bookmarks from the old editorial URLs, without a second body copy."""
    snapshot = ROOT / "archive/editorial/pre-bilingual-2026-10-01"
    old = snapshot / "README.md" if key == "home" else snapshot / "docs" / (key + ".md")
    if not old.is_file():
        return body
    previous = set(re.findall(r'\bid="([^"]+)"', render_markdown(old.read_text())))
    current = set(re.findall(r'\bid="([^"]+)"', body))
    aliases = "".join(f'<span class="legacy-anchor" id="{html.escape(i, quote=True)}"></span>'
                      for i in sorted(previous - current))
    return aliases + body


def page(body, title, destination, lang="en", key=None, redirect=None):
    publication = json.loads((ROOT / "data/publication.json").read_text())
    date = publication.get("publication_date", "")
    release_label = ("初回公開 " if lang == "ja" else "First published ") + date + " · v0.1.0"
    def link(p):
        return quote(os.path.relpath(p, destination.parent), safe="/-_.~")
    css_revision = hashlib.sha256((ROOT / "assets/site.css").read_bytes()).hexdigest()[:12]
    stylesheet = f"{link('assets/site.css')}?v={css_revision}"
    links = "".join(f'<a href="{link(route(lang,k))}"'+(' aria-current="page"' if k==key else '')+f'>{label}</a>' for label,k in NAV[lang])
    pair_key = key or "source-map"
    language_links = " | ".join(
        f'<a lang="{lc}" hreflang="{lc}" href="{link(route(lc,pair_key))}"'+
        (' aria-current="page"' if lc==lang and key else '')+f'>{label}</a>'
        for lc,label in (("ja","日本語"),("en","English")))
    canonical = url_for(route(lang,key)) if key else url_for(destination)
    alternates = "".join(f'<link rel="alternate" hreflang="{lc}" href="{url_for(route(lc,key))}">' for lc in LANGUAGES) if key else ""
    if key: alternates += f'<link rel="alternate" hreflang="x-default" href="{url_for(route("ja",key))}">'
    title_suffix = "リーマン予想が解けるか。" if lang=="ja" else "RH Research Log"
    document_title = title if title == title_suffix else f"{title} · {title_suffix}"
    description = "AIを用いた研究記録。リーマン予想は未解決。補助結果、失敗した方針、未証明の課題を記録します。" if lang=="ja" else "AI-assisted research log. Riemann Hypothesis OPEN. Auxiliary results, failed routes, and unresolved gaps."
    skip = "本文へ" if lang=="ja" else "Skip to content"
    nav_label = "主要ページ" if lang=="ja" else "Main navigation"
    brand = "リーマン予想が解けるか。" if lang=="ja" else "RH Research Log"
    foot = "AIを用いた研究記録" if lang=="ja" else "AI-assisted research"
    methods = "方法と証拠" if lang=="ja" else "Evidence & method"
    license_label = "本文 CC BY 4.0 / コード MIT" if lang=="ja" else "CC BY 4.0 text / MIT code"
    redirects = ""
    if redirect:
        target = link(redirect)
        # JavaScript retains query/fragment; meta refresh and a visible link are fallbacks.
        redirects = f'<meta http-equiv="refresh" content="0;url={html.escape(target,quote=True)}">'+"<script>location.replace("+json.dumps(target)+"+location.search+location.hash);</script>"
    evidence_notice = ""
    if not key:
        note = "原文資料：翻訳せず保存しています。上の言語切替は各言語の出典案内へ戻ります。" if lang=="ja" else "Original evidence: retained without translation. The language links return to each language’s source guide."
        evidence_notice = f'<aside class="evidence-note">{note}</aside>'
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(document_title)}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">{alternates}{redirects}
<link rel="stylesheet" href="{stylesheet}">
<script>window.MathJax={{tex:{{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']],tags:'ams'}},options:{{skipHtmlTags:['script','noscript','style','textarea','pre','code']}}}};</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js"></script>
</head><body>
<a class="skip" href="#content">{skip}</a>
<header><div class="masthead"><a class="brand" href="{link(route(lang,'home'))}">{brand}</a><nav class="language-switch" aria-label="Language / 言語">{language_links}</nav></div><nav class="main-nav" aria-label="{nav_label}">{links}</nav></header>
<div class="status-band"><strong>STATUS: RIEMANN HYPOTHESIS OPEN.</strong><span>{html.escape(release_label)}</span></div>
<main id="content">{evidence_notice}{body}</main>
<footer><span>@ykbballer91 · {foot}</span><a href="{link(route(lang,'methodology'))}">{methods}</a><a href="{link(route(lang,'licensing'))}">{license_label}</a></footer>
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
        info = editorial_info(relative)
        legacy = legacy_info(relative)
        content_source = source
        if legacy:
            content_source = ROOT / source_for(*legacy)
        text = content_source.read_text(encoding="utf-8")
        title_match = re.search(r"^#\s+(.+)", text, re.M)
        title = title_match.group(1).strip() if title_match else source.stem
        lang, key = info or legacy or ("ja" if re.search(r"[ぁ-んァ-ン]",text) else "en", None)
        body = rewrite_links(render_markdown(text), content_source, destination, existing)
        if key:
            body = legacy_anchors(body, key)
        target.write_text(page(body,title,destination,lang,key,route(*legacy) if legacy else None),encoding="utf-8")
        rendered += 1
    # One canonical home source; neither root nor the old docs entry maintains a second snapshot.
    home=Path("index.html")
    body='<h1>リーマン予想が解けるか。</h1><p><a href="ja/">日本語ホームへ</a></p>'
    (output/home).write_text(page(body,"リーマン予想が解けるか。",home,"ja","home",route("ja","home")),encoding="utf-8")
    (output / ".nojekyll").write_text("")
    print(json.dumps({"rendered_markdown_pages": rendered, "copied_or_rendered_public_files": len(sources), "output": "_site", "deployment_performed": False}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    build(args.output)
