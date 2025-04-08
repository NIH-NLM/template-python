A bioinformatics Python package scaffold for reproducible science.

The idea here is to make a tool, such as [NSForest](https://github.com/JCVenterInstitute/NSForest), accessible through a **`command-line`** interface and thereby making it accessible to a workflow language such as [Nextflow](https://www.nextflow.io/).

## 🚀 Quickstart
Render a new Python project with a command-line interface (CLI) + continuous integration with GitHub actions (CI) + documentation by Sphinx:

```bash
cookiecutter gh:NIH-NLM/template-python --output-dir=.
```

### ✅ NIH-NLM Example with [NSForest](https://github.com/JCVenterInstitute/NSForest)

As an example of how to use this repository consider these steps.
These are all the steps followed to make the **`nsforest-cli`** repository with this template-python

In this example, we begin at the root directory below which the new templated repository will be created.

**Render the template into this directory**:
```bash
cookiecutter gh:NIH-NLM/template-python --output-dir=.
```

This will because of the template json file [cookiecutter.json](https://github.com/NIH-NLM/template-python/blob/main/cookiecutter.json), will by the tool [cookiecutter](https://cookiecutter.readthedocs.io) will prompt the user to provide the specified input.   In our case, our template-python asks for the following items:

```bash
{
    "project_name": "Example Bioinfo Tool",
    "repo_name": "example-tool",
    "package_slug": "exampletool",
    "author": "NIH/NLM",
    "email": " your email ",
    "python_version": "3.11",
    "render_url": "{% raw %}${{ steps.deployment.outputs.page_url }}{% endraw %}"
}
```

The user can accept all the defaults after specifying a minimum of three items:

*  "project_name": This can have spaces and is a descriptor
*   "repo_name": Since in general this python package template is for making a command-line interface to said package, recommend naming convention would be **'packagename*-cli`**
*  Package_slug": This would be the name of the python package for which you are making a command-line interface.

Accept the **default** value for the **render_url** prompt.

For our example - this is how it was run:

We ran our **cookiecutter** command:
```bash
cookiecutter gh:NIH-NLM/template-python --output-dir=.
```
Which then prompted us for the following 7 values as outlined in the **cookiecutter.json** file:

```bash
You've downloaded /Users/adeslatt/.cookiecutters/template-python before. Is it okay to 
delete and re-download it? [y/n] (y): y
  [1/7] project_name (Example Bioinfo Tool): NSForest CLI
  [2/7] repo_name (example-tool): nsforest-cli
  [3/7] package_slug (exampletool): nsforest
  [4/7] author (NIH/NLM): NIH/NLM
  [5/7] email ( your email ): adeslat@scitechcon.org
  [6/7] python_version (3.11): 
  [7/7] render_url (${{ steps.deployment.outputs.page_url }}): 
(
```
This creates the directory where we said to make it and now if you inspect you will find it is there: 

```bash
ls -la nsforest-cli
```
Populated with the values and ready to begin to be tested and made complete before making a Nextflow workflow.

```bash
ls -la
total 48
drwxr-xr-x@  11 adeslatt  staff   352 Apr  8 12:23 .
drwxr-xr-x@ 111 adeslatt  staff  3552 Apr  8 12:23 ..
drwxr-xr-x@   3 adeslatt  staff    96 Apr  8 12:23 .github
-rw-r--r--@   1 adeslatt  staff   138 Apr  8 12:23 .readthedocs.yaml
-rw-r--r--@   1 adeslatt  staff   277 Apr  8 12:23 Dockerfile
-rw-r--r--@   1 adeslatt  staff   615 Apr  8 12:23 README.md
drwxr-xr-x@   5 adeslatt  staff   160 Apr  8 12:23 docs
-rw-r--r--@   1 adeslatt  staff   157 Apr  8 12:23 environment.yml
-rw-r--r--@   1 adeslatt  staff   108 Apr  8 12:23 pyproject.toml
-rw-r--r--@   1 adeslatt  staff   489 Apr  8 12:23 setup.cfg
drwxr-xr-x@   3 adeslatt  staff    96 Apr  8 12:23 src
```

Running **tree** we see the directory structure created by the template

```bash
 tree 
.
├── Dockerfile
├── README.md
├── docs
│   ├── Makefile
│   ├── conf.py
│   └── index.rst
├── environment.yml
├── pyproject.toml
├── setup.cfg
└── src
    └── nsforest
        ├── __init__.py
        └── cli.py

4 directories, 10 files
```

Four directories and 10 files automatically set up for you in a shared structured format that will allow ease of integration and use as well as documentation template for us to follow.

Note, the files are here on our local computer, but it is **not yet** in GitHub.
So, now we need to create this repository and push these contents to that repository in 4 steps:
* Create
* Commit
* Init
* Push

**Create, commit, init and then push the result**:

First we need to **create** the repository.   For our **nsforest-cli** example this is what we did.

```bash
gh repo create NIH-NLM/nsforest-cli --internal \
  --description "NSForest CLI for use by man and by machine (aka workflow languages such as Nextflow)" \
  --homepage "https://github.com/NIH-NLM/nsforest-cli"
```

Running this command we see the following response:
```bash
gh repo create NIH-NLM/nsforest-cli --internal \
  --description "NSForest CLI for use by man and by machine (aka workflow languages such as Nextflow)" \
  --homepage "https://github.com/NIH-NLM/nsforest-cli"  
✓ Created repository NIH-NLM/nsforest-cli on GitHub
  https://github.com/NIH-NLM/nsforest-cli
```
Confirming we have created the repository on GitHub.

Next, we need to **init** and **commit** this repository to this new repository and **push** the results.

This involves initializing the directory as a GitHub repository, making an initial commit statement and pushing its content onto GitHub:
```bash
git init
git remote add origin https://github.com/NIH-NLM/template-python.git
git add .
git commit -m "Initial scaffold: template-python"
git branch -M main
git push -u origin main
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

MIT License © National Library of Medicine

