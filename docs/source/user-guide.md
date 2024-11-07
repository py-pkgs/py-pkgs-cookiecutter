# User Guide

This section provides a high-level walk through of building a Python packge using the `py-pkgs-cookiecutter` template. For a much more detailed example see [**Python Packages Chapter 3: How to package a Python**](https://py-pkgs.org/03-how-to-package-a-python).

1. Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/1.7.2/) using `pip` or `conda`:

    **Pip**

    ```{prompt} bash
    pip install cookiecutter
    ```

    **Conda**

    ```{prompt} bash
    conda install cookiecutter
    ```

2. Install [`poetry`](https://python-poetry.org/docs/#installation) for your operating system:

    **OS X / Linux / Bash on Windows**

    ```{prompt} bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
    ```

    **Windows Powershell**

    ```{prompt} powershell
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
    ```

3. Generate a Python package file and directory structure.

    ```{prompt} bash
    cookiecutter https://github.com/py-pkgs/py-pkgs-cookiecutter.git
    ```

    > Note: one of the prompts the `cookiecutter` will ask you is if you want to include GitHub Actions (`include_github_actions`). This prompt allows to choose whether you want a continuous integration (CI) or continuous integration and continuous deployment (CI/CD) workflow file for use with GitHub Actions. If you choose to add CI or CI/CD please read [Continuous integration and continuous deployment](#continuous-integration-and-continuous-deployment).

4. Create and activate a virtual environment using `conda`. Read more in [Section 3.5.1: Create a virtual environment](https://py-pkgs.org/03-how-to-package-a-python#create-a-virtual-environment) of the Python Packages book.

    ```{prompt} bash
    conda create --name <your-env-name> python=3.11 -y
    conda activate <your-env-name>
    ```

    ```{note}
    If you don't create a `conda` virtual environment, `poetry`'s will create one for you using `venv`. You will have to explicitly tell `poetry` to use this virtual environment when runnings commands by prepending them with `poetry run`. Read more in the `poetry` [documentation](https://python-poetry.org/docs/managing-environments/).
    ```

5. Create a repository on GitHub and put your project under local and remote version control (see [Section 3.3: Put your package under version control](https://py-pkgs.org/03-how-to-package-a-python#put-your-package-under-version-control) of the Python Packages book for help).
6. Add Python code to module(s) in the `src/` directory. If your project has dependencies, add them using `poetry`:

    ```{prompt} bash
    poetry add <dependency>
    ```

7. Install and try out your package in a Python interpreter.

    ```{prompt} bash
    poetry install
    ```

8. Write tests for your package in module(s) prefixed with *`test_`* in the *`tests/`* directory. Add `pytest` and `pytest-cov` as development dependencies and calcualte the coverage of your tests. Read more about testing and code coverage in [Section 3.7: Testing your package](https://py-pkgs.org/03-how-to-package-a-python#testing-your-package) of the Python Packages book.

    ```{prompt} bash
    poetry add --dev pytest pytest-cov
    pytest tests/ --cov=<pkg-name>
    ```

9. Create documentation for your package. Add the necessary development depencies listed below and then compile and render documentation to HTML. Read more about testing and code coverage in [Section 3.8: Package documentation](https://py-pkgs.org/03-how-to-package-a-python#package-documentation) of the Python Packages book.

    ```{prompt} bash
    poetry add --dev myst-nb sphinx-autoapi sphinx-rtd-theme
    make html --directory docs/
    ```

10. Host documentation online with [Read the Docs](https://readthedocs.org/). Read more about hosting on Read the Docs in [Section 3.8.5: Hosting documentation online](https://py-pkgs.org/03-how-to-package-a-python#hosting-documentation-online) of the Python Packages book. Alternatively, you can host on [GitHub Pages](https://pages.github.com) using the [ghp-import](https://github.com/c-w/ghp-import) package as follows:

    ```{prompt} bash
    poetry add --dev ghp-import
    ghp-import -n -p -f docs/_build/html
    ```

    ```{note}
    The above command pushes your HTML files to the `gh-pages` branch of your repo. With the rendered site available at e.g., `https://<user-name>.github.io/<repo-name>/`. The `-n` argument includes a *.nojekyll* file in the branch. `-p -f` force pushes to the remote. Read more in the [ghp-import](https://github.com/c-w/ghp-import) documentation.
    ```

11. Tag a release of your package using Git and GitHub, or equivalent version control tools. Read more about tagging releases in [Section 3.8.5: Tagging a package release with version control](https://py-pkgs.org/03-how-to-package-a-python#tagging-a-package-release-with-version-control) of the Python Packages book.

12. Build sdist and wheel distributions for your package.  Read more in [Section 3.10: Building and distributing your package](https://py-pkgs.org/03-how-to-package-a-python#building-and-distributing-your-package) of the Python Packages book.

    ```{prompt} bash
    poetry build
    ```

13. Publish your distributions to [TestPyPi](https://test.pypi.org/) and try installing your package.

    ```{prompt} bash
    poetry config repositories.test-pypi https://test.pypi.org/legacy/
    poetry publish -r test-pypi
    pip install --index-url https://test.pypi.org/simple/ <pkg-name>
    ```

14. Publish your distributions to [PyPi](https://pypi.org/). Your package can now be installed by anyone using `pip`.

    ```{prompt} bash
    poetry publish
    pip install <pkg-name>
    ```

## Releasing new versions of your package

The process for releasing new versions of your package is described in detail in [Chapter 7: Releasing and Versioning](https://py-pkgs.org/07-releasing-versioning) of the Python Packages book.

## Continuous integration and continuous deployment

One of the prompts the `cookiecutter` will ask you is if you want to include GitHub Actions (`include_github_actions`). This prompt allows to choose whether you want a continuous integration (CI) or continuous integration and continuous deployment (CI/CD) workflow file for use with GitHub Actions. The possible responses are described in the following sections. You can read more about CI/CD and these workflow files in [Chapter 8: Continuous integration and deployment](https://py-pkgs.org/08-ci-cd) of the Python Packages book.

### No

A GitHub Actions workflow file won't be included in your package structure.

### CI (continuous integration)

A GitHub Actions workflow file for continuous integration will be included in your package structure at `.github/workflows/ci.yml`. It contains the following features:

- Triggered on "push" or "pull request" to the `main` branch.
- Sets up a Ubuntu operating system, checks out your repository, installs Python 3.9, and installs the latest version of `poetry`.
- Installs your package with `poetry install`
- Runs test with `pytest tests/`
- Upload code coverage of tests to Codecov
- Builds documentation with `sphinx`

### CI+CD (continuous integration + continuous deployment)

A GitHub Actions workflow file for continuous integration and continuous deployment will be included in your package structure at `.github/workflows/ci-cd.yml`. It contains the following features:

- CI job:
  - Same as described above.
- CD job:
  - Triggered on a "push" or merged "pull request" to the `main` branch.
  - Sets up a Ubuntu operating system, checks out your repository, installs Python 3.9.
  - Uses [Python Semantic Release (PSR)](https://github.com/relekang/python-semantic-release) to automatically bump version numbers based on commit messages. PSR will also update the CHANGELOG, tag a new release of the repository, and build new sdist and wheel distributions ready to upload to PyPI. Read more PSR in [Section 8.5.2: Automatically creating a new package version](https://py-pkgs.org/08-ci-cd#automatically-creating-a-new-package-version) of the Python Packages book.
  - Publishes new distributions to TestPyPI. For this to work, you'll need to log-in to [TestPyPI](https://test.pypi.org), [create an API token](https://pypi.org/help/#apitoken), and [add the token as a secret](https://docs.github.com/en/actions/reference/encrypted-secrets) called `TEST_PYPI_API_TOKEN` to your GitHub repository.
  - Tests that the new distributions install successfuly from TestPyPI using `pip install`
  - Publishes distributions to PyPI. For this to work, you'll need to log-in to [PyPI](https://pypi.org), [create an API token](https://pypi.org/help/#apitoken), and [add the token as a secret](https://docs.github.com/en/actions/reference/encrypted-secrets) called `PYPI_API_TOKEN` to your GitHub repository.
