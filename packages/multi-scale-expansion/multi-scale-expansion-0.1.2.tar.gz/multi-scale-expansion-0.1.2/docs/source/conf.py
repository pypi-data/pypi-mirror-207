import sys, os	
import sphinx_rtd_theme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'multi-scale-expansion'
copyright = '2023, Angel Mancera'
author = 'Angel Mancera'
release = '0.1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'recommonmark'] # , 'sphinx.ext.napoleon'
source_suffix = ['.rst', '.md']
# napoleon_google_docstring = False
# napoleon_use_param = False
# napoleon_use_ivar = True

sys.path.insert(0, os.path.abspath('../'))
templates_path = ['_templates']
exclude_patterns = ['modules.rst']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
