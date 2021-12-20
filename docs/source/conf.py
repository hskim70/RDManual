# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Sphinx Tutorial'
copyright = '2021, Sun Kim'
author = 'Sun Kim'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'fluiddoc.mathmacro',
'sphinx.ext.autosectionlabel',
#'sphinxprettysearchresults'
#'sphinx_search.extension',
#'sphinx.ext.mathjax'
#'sphinx.ext.imgmath',
#'sphinxcontrib.osexample'
]

#'sphinx.ext.autosectionlabel',
# Make sure the target is unique
autosectionlabel_prefix_document = True

#use_old_search_snippets = True

#sphinx.ext.imgmath
#imgmath_image_format = 'png'

#mathjax_path ="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"

#http://docs.itascacg.com/pfc600/common/docproject/utilities/icgsphinxhelp/icgsphinxhelp_system.html
#mathjax_path = 'MathJax/MathJax.js?config=TeX-AMS_SVG'   #for local library appears on a line by itself


#pip install fluiddoc
#pip install sphinxcontrib-osexample

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s', 'code-block': 'Listing %s', 'section': 'Section %s'}
numfig_secnum_depth = 1

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'classic'
#html_theme = 'sphinxdoc'
#html_theme = 'scrolls'
#html_theme = 'agogo'
#html_theme = 'traditional'
#html_theme = 'nature'
#html_theme = 'haiku'
#html_theme = 'pyramid'
#html_theme = 'bizstyle'
html_theme = 'sphinx_rtd_theme'
#html_theme = 'furo'
#html_theme = 'press'
#html_theme = 'karma_sphinx_theme'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#//https://docs.restructuredtext.net/articles/configuration.html

#Equation numbering aling center to right
#https://github.com/qutip/qutip/pull/1678/commits/59cc57a682a0d43f38cc2f1251ebed7678070761
html_css_files = [
    'site.css',
#    'my_theme.css'
]

#https://stackoverflow.com/questions/45969711/sphinx-doc-how-do-i-render-an-animated-gif-when-building-for-html-but-a-png-wh
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]
