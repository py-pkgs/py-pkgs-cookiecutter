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

1. Install the latest Cookiecutter if you haven't installed it yet (this
requires Cookiecutter 1.4.0 or higher)

   ```
   pip install -U cookiecutter
   ```

2. Generate a Python package file and directory structure:
   ```
   cookiecutter https://github.com/UBC-MDS/cookiecutter-ubc-mds.git
   ```

3. Initialize it with Poetry. Adding the following dev dependencies when prompted:
   - pytest
   - pytest-cov
   - codecov
   - flake8
   - sphinx

   ```
   cd <your_project>
   poetry init
   ```

4. Create a remote version control repository on GitHub for this project, and link it to <https://codecov.io/>. Get the repository token from <https://codecov.io/> and record is as a secret on GitHub using the name `CODECOV_TOKEN`.
    
5. Write the code and tests for your Python package! And use Python poetry to install, add dependencies and test your package locally. For more details, see the [py-pkgs book](https://ubc-mds.github.io/py-pkgs/).

6. Put your local files under version control with Git, add the GitHub repository you set up as the remote and push your changes to GitHub! 

7. When you are satisfied, use poetry to publish your package to testPyPI.


#### Optional (automated version bumping and release to test PyPI)

8. Add the following to the `pyproject.toml` file (substituting <your_project> with the appropriate value):
   ```
   [tool.semantic_release]
   version_variable = "<your_project>/__init__.py:__version__"
   version_source = "commit"
   upload_to_pypi = "false"
   patch_without_tag = "true"
   ```

9. Add the following secrets to the project's repository on GitHub:
   - PYPI_USERNAME
   - PYPI_PASSWORD

10. Put your local files under version control with Git, add the GitHub repository you set up as the remote and push your changes to GitHub and Let the magic happen!

For more details, see the [py-pkgs book](https://ubc-mds.github.io/py-pkgs/).

### Credits

This template was modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
