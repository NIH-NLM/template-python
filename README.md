# {{ project_name }}

A bioinformatics Python package scaffold for reproducible science.

## 🚀 Quickstart
```bash
cookiecutter gh:NIH-NLM/template-python
```

## 📦 Features
- Typer-based CLI
- Dockerized
- Sphinx auto docs
- GitHub Actions CI (tests, docs, Docker)
- Pytest + Conda
- GitHub Container Registry (GHCR) integration

## 🐳 GitHub Container Registry (GHCR)
This template includes a workflow to automatically build and publish Docker images to [GitHub Container Registry (GHCR)](https://github.com/features/packages).

### 🛠 GHCR Docker Image Publishing
- Image is built and pushed on commits to `main`
- Image URL format: `ghcr.io/OWNER/REPO:latest`

### 🔐 To make image public (optional):
```bash
gh api \
  -X PATCH \
  -H "Accept: application/vnd.github.v3+json" \
  /user/packages/container/{{ cookiecutter.package_slug }}/visibility \
  -f visibility=public
```

## Directory Structure

```
template-python/
├── .github/
│   └── workflows/
│       ├── test.yml            # Run tests on push
│       ├── docs.yml            # Auto-build + deploy docs
│       └── docker.yml          # Optional: Docker image CI/CD
│
├── docs/
│   ├── conf.py                 # Sphinx config
│   ├── index.rst               # Sphinx docs home
│   └── Makefile                # Build command
│
├── src/{{ package_slug }}/     # Actual package code
│   ├── __init__.py
│   ├── cli.py                  # CLI commands via Typer
│   ├── core.py                 # Core functions (placeholder)
│   └── utils.py                # Shared logic/utilities
│
├── tests/
│   └── test_cli.py             # Sample pytest CLI test
│
├── .readthedocs.yaml           # RTD config
├── Dockerfile                  # Conda + pip + CLI ready
├── environment.yml             # Conda environment
├── pyproject.toml              # Modern Python packaging
├── setup.cfg                   # Metadata, CLI entry point
├── cookiecutter.json           # Cookiecutter template variables
├── README.md
└── LICENSE
```

## Example Projects Using This Template
- [`scsilhouette`](https://github.com/NIH-NLM/scsilhouette)
- Upcoming: [`nsforest-cli`](https://github.com/NIH-NLM/nsforest-cli)

This pattern supports reusable tool wrapping for Nextflow and CLI use cases.

---

## 🛠 Template Design and Publication
This repository structure was designed by NIH developers for modular bioinformatics workflows.
The template was scaffolded with the assistance of ChatGPT Code Copilot.

### To publish this repository to GitHub:

Start by creating the repository **if it does not yet exist**:
```bash
gh repo create NIH-NLM/template-python --public \
  --description "Reusable Python CLI + container template for bioinformatics tools" \
  --homepage "https://github.com/NIH-NLM/template-python" \
  --confirm
```

Then initialize and push:
```bash
git init
git remote add origin https://github.com/NIH-NLM/template-python.git
git add .
git commit -m "Initial scaffold: template-python"
git branch -M main
git push -u origin main
```

MIT License © National Library of Medicine

