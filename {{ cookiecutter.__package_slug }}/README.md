# {{ cookiecutter.__package_slug }}

{{ cookiecutter.package_short_description }}

## Installation

```bash
$ pip install {{ cookiecutter.__package_slug }}
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`{{ cookiecutter.__package_slug }}` was created by {{ cookiecutter.author_name }}. {% if cookiecutter.open_source_license != 'None' -%}It is licensed under the terms of the {{ cookiecutter.open_source_license }} license.{% else %}{{ cookiecutter.author_name }} retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.{% endif %}

## Credits

`{{ cookiecutter.__package_slug }}` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
