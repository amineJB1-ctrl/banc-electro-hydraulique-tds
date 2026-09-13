# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'Banc électro-hydraulique'
copyright = '2026, Mohamed Amine jabeur / Nour Miladi'
author = 'Mohamed Amine Jabeur / Nour Miladi'
release = '1.0'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Numérotation des figures
numfig = True

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_baseurl = "https://amineJB1-ctrl.github.io/banc-electrohydraulique/"

html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 4,
}
