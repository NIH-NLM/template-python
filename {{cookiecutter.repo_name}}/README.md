# {{cookiecutter.project_name}}

A command-line bioinformatics tool scaffolded using [template-python](https://github.com/NIH-NLM/template-python).

---

## 🛠 Features

- Python {{cookiecutter.python_version}}
- Typer-powered CLI
- Conda + Docker compatible
- CI with GitHub Actions
- Auto-generated Sphinx docs

---

## 🚀 Getting Started

Install via Conda or use Docker:

```bash
conda env create -f environment.yml
conda activate {{cookiecutter.package_slug}}
# OR
docker build -t {{cookiecutter.package_slug}} .
docker run -it {{cookiecutter.package_slug}}
```

---

## 💡 CLI Usage

```bash
{{cookiecutter.package_slug}} --help
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 📄 License

MIT License © {{cookiecutter.author}}

