from {{cookiecutter.__package_slug}}.example import nchar


def test_nchar_returns_none():
    expected = None
    assert nchar("") == expected


def test_nchar_returns_number_characters():
    expected = 9
    assert nchar("Data team") == expected
