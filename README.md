A bioinformatics Python package scaffold for reproducible science.

## 🚀 Quickstart
Render a new Python project with CLI + CI + Docs:

```bash
cookiecutter gh:NIH-NLM/template-python
```

### ✅ NIH-NLM Recommended Usage (Security-Aware)

As an example of how to use this repository consider these steps.
These are all the steps followed to make the nsforest-cli repository with this template-python

If you must create the repository *before* rendering:

1. **Create your GitHub repo manually** in the NIH-NLM org
   (e.g. https://github.com/NIH-NLM/nsforest-cli)

2. **Clone it locally**:
```bash
git clone https://github.com/NIH-NLM/nsforest-cli.git
cd nsforest-cli
```

3. **Render the template into this directory**:
```bash
cookiecutter gh:NIH-NLM/template-python --output-dir=.
```

4. **Commit and push the result**:
```bash
git add .
git commit -m "Initial scaffold from template"
git push
```

### 🛠 Cookiecutter Troubleshooting
If you see this error:
```
JSON decoding error while loading '/Users/.../.cookiecutters/template-python/cookiecutter.json'
```
You likely have a corrupted cached copy of the template.

✅ Fix it by removing the local template cache:
```bash
rm -rf ~/.cookiecutters/template-python
```
Then retry:
```bash
cookiecutter gh:NIH-NLM/template-python --output-dir=.
```

## 📦 Features
- Typer-based CLI
- Dockerized
- Sphinx auto docs
- GitHub Actions CI (tests, docs, Docker)
- Pytest + Conda
- GitHub Container Registry (GHCR) integration

## ⚠️ Important: Do Not Run CI from This Template Repo
This repository contains unrendered `{{ cookiecutter.* }}` placeholders.
GitHub Actions **will fail** if triggered directly.

✅ **Always render first** using Cookiecutter.

---

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

## Example Projects Using This Template
- [`nsforest-cli`](https://github.com/NIH-NLM/nsforest-cli)

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

