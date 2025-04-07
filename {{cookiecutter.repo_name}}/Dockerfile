# Dockerfile
FROM continuumio/miniconda3
WORKDIR /app
COPY . .
RUN conda env create -f environment.yml && \
    echo "source activate {{cookiecutter.package_slug}}" > ~/.bashrc
ENV PATH /opt/conda/envs/{{cookiecutter.package_slug}}/bin:$PATH
ENTRYPOINT ["{{cookiecutter.package_slug}}"]

# src/{{cookiecutter.package_slug}}/__init__.py
"""{{cookiecutter.package_slug}} package."""

