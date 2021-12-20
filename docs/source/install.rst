Install Guide
#############

install python
**************

- python 3.9.6 or later
 
   svn://fbserver/Common/Document/Sphinx/trunk/lib/python-3.9.6-amd64.exe

   check Add Path during install python

   .. image:: Tutorial_Sphinx/media/install_python.png

install shpinx
**************

- dos command

   .. code-block::

       >pip install sphinx
       >pip install sphinx-autobuild

install vscode
**************

- vscode 1.62 or later

   svn://fbserver/Common/Document/Sphinx/trunk/lib/VSCodeUserSetup-x64-1.62.0.exe

install vscode extension
************************

install Extension Pack for RestructuredText
===========================================

- run vscode

- search extension "Extension Pack for RestructuredText"
   
   .. image:: Tutorial_Sphinx/media/rest.png

- install "Extension Pack for RestructuredText"

install reStructuredText Syntax highlighting
============================================

- search extension "reStructuredText Syntax highlighting"

   .. image:: Tutorial_Sphinx/media/rest_highlight.png

- install "reStructuredText Syntax highlighting"

install Preview
===============

- search extension "Preview"

   .. image:: Tutorial_Sphinx/media/preview.png

- install "Preview"

- to use preview, select ``*.rst``, press Ctrl-Shift-R

   .. image:: Tutorial_Sphinx/media/preview_2nd.png


Run VS Code
***********

- restart vscode

- open folder in vscode

   .. image:: Tutorial_Sphinx/media/openfolder.png
      

   select Sphinx SVN folder such as ``D:\SVNSource\Document\Sphinx\trunk\SphinxTutorial``

- edit conf.py,  if you are document manager

- edit index.rst, if you are document manager

- edit ``install.rst`` to update installation process

- edit ``Tutorial_Sphinx\Tutorial_Sphinx.rst`` to update Sphinx Tutorial