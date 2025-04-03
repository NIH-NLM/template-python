# Dockerfile
FROM continuumio/miniconda3
WORKDIR /app
COPY . .
RUN conda env create -f environment.yml && \
    echo "source activate {{ package_slug }}" > ~/.bashrc
ENV PATH /opt/conda/envs/{{ package_slug }}/bin:$PATH
ENTRYPOINT ["{{ package_slug }}"]

# src/{{ package_slug }}/__init__.py
"""{{ project_name }} package."""

