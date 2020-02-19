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

Add local and remote version control using Git & GitHub for this project and ensure the following secrets are recorded on GitHub:
- CODECOV_TOKEN
- PYPI_USERNAME
- PYPI_PASSWORD

For more details, see the [Whole Game Chapter](https://ubc-mds.github.io/py-pkgs/whole-game.html) of the [py-pkgs book](https://ubc-mds.github.io/py-pkgs/)

### Credits

This template was modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
