# Hello World · Python on GitHub Pages

A small Python-generated website, published automatically to GitHub Pages.

## Local development

```bash
python build_site.py
python -m unittest -v
python -m http.server 8000 --directory docs
```

Then open <http://localhost:8000>.

## Deployment

Every push to `main` runs `.github/workflows/pages.yml`. The workflow generates `docs/index.html` with Python and deploys it using the official GitHub Pages Actions.

Live site: <https://renatco.github.io/hello-world-python-site/>

The repository is private; GitHub Pages availability for private repositories depends on the account or organization plan.
