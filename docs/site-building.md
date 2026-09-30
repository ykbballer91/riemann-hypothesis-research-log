# Build and inspect the documentation site

**STATUS: RIEMANN HYPOTHESIS OPEN**

The site is generated from the same Markdown files used on GitHub. A small Python builder converts internal Markdown links to HTML links and protects TeX while Markdown is parsed. MathJax 3.2.2 renders the formulas in the browser; it is loaded from the public jsDelivr CDN rather than vendored.

From the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-site.txt
.venv/bin/python tools/build_site.py
.venv/bin/python tools/validate_public.py --site
python3 -m http.server 8765 --bind 127.0.0.1 --directory _site
```

Open the local server's port 8765 in a browser. The generated `_site` directory and the virtual environment are ignored by Git. The build includes only the public document, archive, artifact, data, and tooling directories plus an explicit list of publication-review reports. Full local audit inventories are excluded.

`validate_public.py` checks local file links and section anchors, JSON syntax, source/export manifest hashes, the OPEN banner, the citation's author display and absent release date, and the Pages deployment guard. It does not crawl every external citation, execute historical mathematical experiments, or certify the mathematics.

## GitHub Pages guard

The workflow builds on a push to `main` and uploads a Pages artifact. It **does not deploy from a private repository**. Deployment also requires a manual workflow dispatch with `deploy=true` and the repository variable `PUBLICATION_APPROVED=true`. Those guards are not a request to change visibility now.

Public visibility, the actual public release date, the approval variable, and a live Pages deployment belong to a later creator-approved publication step. A build artifact is not a published website. Availability of Pages for private repositories depends on the account plan; this phase does not rely on private Pages hosting.

The workflow uses the official [GitHub Pages actions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), pinned to inspected revisions. There is no separate application framework or database.

