# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import datetime

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = "py-pkgs-cookiecutter"
author = "Tomas Beuzen & Tiffany Timbers"
copyright = f"{datetime.datetime.now().year}, Tomas Beuzen & Tiffany Timbers"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["myst_parser", "sphinx_rtd_theme", "sphinx-prompt", "sphinx_copybutton"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
def setup(app):
    app.add_css_file("custom.css")  # may also be an URL


html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"
html_logo = "_static/logo.png"
