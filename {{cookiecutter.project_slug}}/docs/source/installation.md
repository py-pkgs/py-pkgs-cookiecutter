# Installation


## Installing from PyPI

``{{ cookiecutter.project_slug }}`` can be installed from PyPI using `pip`:

```console
$ pip install {{ cookiecutter.project_slug }}
```

This is the preferred method to install ``{{ cookiecutter.project_slug }}``, as it will always install the most recent stable release.

If you don't have `pip` installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide
you through the process.

## Installing from source

You can install the latest development version of ``{{ cookiecutter.project_slug }}`` by cloning the [GitHub repository](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}) and using `poetry` to install from the local directory:

```console
$ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
$ cd {{ cookiecutter.project_slug }}
$ poetry install
```