# Build and inspect the bilingual site

**STATUS: RIEMANN HYPOTHESIS OPEN**

The Markdown editorial sources live under `docs/ja/` and `docs/en/`. The builder maps matching source names to `/ja/` and `/en/` routes. Each page has a paired language switch, a language-specific navigation bar, a canonical URL, `html lang`, and reciprocal `hreflang` links. The source key `index` maps to `guide`, `source-map` to `sources`, and `home` to the language root.

The root and old `/docs/*.html` URLs are compatibility pages, generated from the canonical language source with a redirect and a visible fallback. They do not maintain a separate latest-state snapshot. Redirects retain the query and fragment in JavaScript. Historical anchor aliases are preserved. The unmodified research-state record remains the source of status metadata; this editorial reorganization does not update research claims.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-site.txt
.venv/bin/python tools/build_site.py
.venv/bin/python tools/validate_public.py --site
.venv/bin/python tools/validate_bilingual.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory _site
```

The generated `_site` and virtual environment are ignored by Git. TeX is protected during Markdown parsing, then rendered by MathJax 3.2.2 from jsDelivr. Wide formulas and tables scroll inside their own containers rather than widening the page.

## Editorial and evidence boundaries

Every editorial source must have a counterpart with the same filename. Research reports, audits, artifacts, and source records retain their original language. The existing 378-entry source manifest and exported evidence hashes are unchanged. Pre-restructure public prose is retained in `archive/editorial/pre-bilingual-2026-10-01/` with portable links; it is historical editorial evidence, not a new mathematical result.

The public validator checks local links and anchors, JSON, source-manifest hashes, OPEN status, authorship and release dates, and the deployment guard. The bilingual validator additionally checks paired routes, language metadata, navigation, current-state agreement, and compatibility URLs. Neither proves mathematics or reruns research experiments. Mobile viewport and anonymous deployment checks are recorded in the [editorial review](../../audit/bilingual_review.md).

## GitHub Pages deployment

A push to `main` builds and validates the site. Deployment additionally requires an explicit workflow dispatch with `deploy=true`, a public repository, and `PUBLICATION_APPROVED=true`. The existing guard remains. A build artifact alone is not a published site. The workflow uses the official [GitHub Pages actions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), pinned to inspected revisions.
