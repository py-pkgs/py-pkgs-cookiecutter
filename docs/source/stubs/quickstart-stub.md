Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/):

```{prompt} bash
pip install cookiecutter
```

Generate a Python package structure using [`py-pkgs-cookiecutter`](https://github.com/py-pkgs/py-pkgs-cookiecutter):

```{prompt} bash
cookiecutter https://github.com/py-pkgs/py-pkgs-cookiecutter.git
```

```text
pkg
├── .github                    ┐
│   └── workflows              │ GitHub Actions workflow
│       └── ci-cd.yml          ┘
├── .gitignore                 ┐
├── .readthedocs.yml           │
├── CHANGELOG.md               │
├── CONDUCT.md                 │
├── CONTRIBUTING.md            │
├── docs                       │
│   ├── make.bat               │
│   ├── Makefile               │
│   ├── requirements.txt       │
│   ├── changelog.md           │
│   ├── conduct.md             │
│   ├── conf.py                │ Package documentation
│   ├── contributing.md        │
│   ├── index.md               │
│   └── usage.ipynb            │
├── LICENSE                    │
├── README.md                  ┘
├── pyproject.toml             ┐ 
├── src                        │
│   └── pkg                    │ Package source code, metadata,
│       ├── __init__.py        │ and build instructions 
│       └── pkg.py             ┘
└── tests                      ┐
    └── test_pkg.py            ┘ Package tests
```
