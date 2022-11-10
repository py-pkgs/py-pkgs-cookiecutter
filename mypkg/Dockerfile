FROM python:3.8.13-slim-buster
WORKDIR /app
COPY src /app/src
COPY pyproject.toml /app/pyproject.toml
COPY README.md /app/README.md

RUN pip install .

ENTRYPOINT [ "pipeline" ]
