# Installation


## Stable release

To install ``{{ cookiecutter.project_slug }}``, run this command in your terminal:

```console
$ pip install {{ cookiecutter.project_slug }}
```

This is the preferred method to install ``{{ cookiecutter.project_slug }}``, as it will always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide
you through the process.

## From sources

The source for ``{{ cookiecutter.project_slug }}`` can be downloaded from the [Github repo](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}).

You can either clone the public repository:

```console
$ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```

Or download the [tarball](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/main):

```console
$ curl  -OL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/main
```

Once you have a copy of the source, you can install it. The method of installation will depend on the packaging library being used.

For example, if [setuptools](https://setuptools.readthedocs.io/en/latest/) is being used (a ``setup.py`` file is present), install ``{{ cookiecutter.project_slug }}`` with:

```console
$ python setup.py install
```

If [poetry](https://python-poetry.org) is being used (``poetry.lock`` and ``pyproject.toml`` files are present), install ``{{ cookiecutter.project_slug }}`` with:

```console
$ poetry install
```
