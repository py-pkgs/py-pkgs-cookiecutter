## Cookiecutter UBC-MDS

**Cookiecutter** template for a UBC-MDS Python packge.
-  Free software: BSD license

### Features

-  **pytest** testing: Setup to easily test for Python 3.7 & 3.8 (other Python versions can be added by editing the GitHub Actions workflow file)
-  **GitHub Actions**: Ready for GitHub Actions Continuous Integration testing & Deployment
-  **codecov**: Code coverage report and badge using codecov and GitHub Actions
-  **Sphinx** docs: Documentation ready for generation with, for
   example, **ReadTheDocs**
-  **Python-semantic-release**: Pre-configured version bumping upon merging pull request to master
-  Auto-release to **testPyPI** upon merging pull request to master

### Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this
requires Cookiecutter 1.4.0 or higher)

```
pip install -U cookiecutter
```

Generate a Python package file and directory structure:
```
cookiecutter https://github.com/UBC-MDS/cookiecutter-ubc-mds.git
```

Initialize it with Poetry:
```
cd <your_project>
poetry init
```

#### Optional (automated version bumping and release to test PyPI)

Add the following to the `pyproject.toml` file (substituting <your_project> with the appropriate value):
```
[tool.semantic_release]
version_variable = "<your_project>/__init__.py:__version__"
version_source = "commit"
upload_to_pypi = "false"
patch_without_tag = "true"
```

Create a remote version control repository on GitHub for this project and ensure the following secrets are recorded on GitHub:
- CODECOV_TOKEN
- PYPI_USERNAME
- PYPI_PASSWORD

Login to <https://codecov.io/> and link the GitHub repository to Codecov.

Put your local files under version control with Git, add the GtiHub repository you set up as the remote and push your changes to GitHub!

For more details, see the [Whole Game Chapter](https://ubc-mds.github.io/py-pkgs/whole-game.html) of the [py-pkgs book](https://ubc-mds.github.io/py-pkgs/)

### Credits

This template was modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
