FROM python:{{ cookiecutter.python_version }}-slim-buster
WORKDIR /app
COPY src /app/src
COPY pyproject.toml /app/pyproject.toml
COPY README.md /app/README.md

RUN pip install .

ENTRYPOINT [ "pipeline" ]
