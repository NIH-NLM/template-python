# docs/conf.py
project = '{{cookiecutter.package_slug}}'
author = '{{cookiecutter.author}}'
release = '0.1.0'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
exclude_patterns = []
templates_path = ['_templates']
html_theme = 'alabaster'
html_static_path = ['_static']

