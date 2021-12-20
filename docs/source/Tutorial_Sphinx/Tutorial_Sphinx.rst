
RestructuredText Tutorial 
#########################

Section Headings
**************************

.. code-block:: 
   :caption: Section Numbers are made by Headings
   :name: Headings

   Sphinx Tutorial 2 - Part
   ########################

   List 2.1 - Chapter
   ******************

   Unordered List 2.1.1 - Section
   ==============================

   Heading4 2.1.1.1 - Subsection
   -----------------------------

   Heading5 2.1.1.1.1 - Subsubsection
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Heading6 2.1.1.1.1.1 - paragraph
   ''''''''''''''''''''''''''''''''

Inline Formatting
*****************

*italic text*  ``*italic text*`` 

**bold text**  ``**bold text**`` 

inline literal: select ``*.rdyn`` file. ````*.rdyn````

A :sup:`i,j` ``A :sup:`i,j```

A :sub:`i,j` ``A :sub:`i,j```

GUI Label: :guilabel:`Open Model` ``:guilabel:`Open Model```

GUI Menu: :menuselection:`File > Open > *.rdyn` ``:menuselection:`File > Open > *.rdyn```

File: :file:`*.rdyn` ``:file:`*.rdyn``` 

Keyboard: :kbd:`ctrl` + :kbd:`s` ``:kbd:`ctrl` + :kbd:`s```

.. .. code-block::

..    :file:`*.rdyn`

..    :kbd:`ctrl` + :kbd:`s`

.. Keyboard combination Press ``Ctrl+s`` to save model. ````Ctrl+s````

.. this is a Comment
.. with another line

.. this is a Comment
   with another line

.. code-block::

   .. this is a Comment
   .. with another line

   .. this is a Comment
      with another line


List
**************************

Unordered List
==============

- Unordered item1
  
   - nested unordered item1
   - nested unordered item2

- Unordered item2

   #. nested ordered item1
   #. nested ordered item2

Ordered List
============

#. Numbers are auto generated

   - sub item1
   - sub item2

#. a, b, c ordered

   a. nested ordered item1
   #. nested ordered item2


Image 
**************************

.. image:: media/rd001.jpg 
   
this is image.

.. |rd001| image:: media/rd001.jpg

image inside of the text. |rd001| like this.

images in the list

- item1
   .. image:: media/rd002.png

- item2

   - sub item1
         .. image:: media/rd002.png


Table
****************************

Simple Table
========================

.. table:: Simple Table
   :name: simpletable

   =====  =====  ======
      Inputs     Output
   ------------  ------
   A      B      A or B
   =====  =====  ======
   False  False  False
   True   False  True
   False  True   True
   True   True   True
   =====  =====  ======


.. code-block::

   .. table:: Simple Table
      :name: simpletable

      =====  =====  ======
         Inputs     Output
      ------------  ------
      A      B      A or B
      =====  =====  ======
      False  False  False
      True   False  True
      False  True   True
      True   True   True
      =====  =====  ======


Grid Table
========================

.. table:: Grid Table
   :name: gridtable

   +------------+------------+-----------+
   | Header 1   | Header 2   | Header 3  |
   +============+============+===========+
   | body row 1 | column 2   | column 3  |
   +------------+------------+-----------+
   | body row 2 | Cells may span columns.|
   +------------+------------+-----------+
   | body row 3 | Cells may  | - Cells   |
   +------------+ span rows. | - contain |
   | body row 4 |            | - blocks. |
   +------------+------------+-----------+

.. code-block::

   .. table:: Grid Table
      :name: gridtable

      +------------+------------+-----------+
      | Header 1   | Header 2   | Header 3  |
      +============+============+===========+
      | body row 1 | column 2   | column 3  |
      +------------+------------+-----------+
      | body row 2 | Cells may span columns.|
      +------------+------------+-----------+
      | body row 3 | Cells may  | - Cells   |
      +------------+ span rows. | - contain |
      | body row 4 |            | - blocks. |
      +------------+------------+-----------+

List Table
========================
    
.. list-table:: List Table
   :header-rows: 1
   :name: listtable
   :widths: 25 25 50

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     

.. code-block::

   .. list-table:: List Table
      :header-rows: 1
      :name: table2
      :widths: 25 25 50

      * - Heading row 1, column 1
      - Heading row 1, column 2
      - Heading row 1, column 3
      * - Row 1, column 1
      -
      - Row 1, column 3
      * - Row 2, column 1
      - Row 2, column 2
      - Row 2, column 3


CSV Table
=========
     
.. csv-table:: csv table without file
   :name: table3

   Header1, Header2, Header3
   1,2,3
   "1, 2", "2, 3, 4", "3, 4"
   "1, 2", "2, 3", "3, 4"


.. code-block::

   .. csv-table:: csv table without file
      :name: table3

      Header1, Header2, Header3
      1,2,3
      "1, 2", "2, 3, 4", "3, 4"
      "1, 2", "2, 3", "3, 4"


.. .. csv-table:: csv table with file
..    :file: csvtable.csv
..    :name: table4

.. .. code-block::

..    .. csv-table:: csv table with file
..       :file: csvtable.csv
..       :name: table4


Target and Links
****************

Internal Links (Anchor)
==========================

.. :ref:`Target and Links`

.. :ref:`Internal Links (Anchor)`

:ref:`Tutorial_Sphinx/Tutorial_Sphinx:Target and Links`

:ref:`Tutorial_Sphinx/Tutorial_Sphinx:Internal Links (Anchor)`

.. code-block::

   :ref:`Target and Links`
   :ref:`Internal Links (Anchor)`

.. code-block::

   .. _RST Overview:

   Overview
   **********

   RST Overview content


   .. _Sphinx Overview:

   Overview
   *********

   Sphinx Overview content

   This is a link to the RST Overview: :ref:`RST Overview`

   This is a link to the Sphinx Overview: :ref:`Sphinx Overview`


External Links
==============

`FunctionBay <http://www.functionbay.co.kr>`_

.. code-block::
   
   `FunctionBay <http://www.functionbay.co.kr>`_

RecurDyn homepage is RecurDyn_.

.. _RecurDyn: http://www.recurdyn.com

.. code-block::

   RecurDyn homepage is RecurDyn_.

   .. _RecurDyn: http://www.recurdyn.com


Footnote
==============

auto numbered footnotes

footnotes1 [#f1]_ and footnotes2 [#f2]_

.. [#f1] A footnote1
.. [#F2] A footnote2

.. code-block::

   footnotes1 [#f1]_ and footnotes2 [#f2]_

   .. [#f1] A footnote1
   .. [#F2] A footnote2


Citation
==============

Look Reference [Ref]_ and this [paper1]_.

.. [Ref] Book or article reference, URL or whatever.

.. [paper1] A global citation



Code Block
**************************

.. code-block::
   :caption: C# code
   :name: code_c#1
   
   var i = 1;
   var str = $"test{i}";

.. code-block::
   :caption: C# with line number
   :name: code_c#2
   :linenos:   
   
   var i = 1;
   var str = $"test{i}";


.. Literal Block
.. ****************

.. Assign the variable a::

..    $a = 'hello';

..    $b = 'world';

.. .. code-block::   

..    Assign the variable a::

..       $a = 'hello';

..       $b = 'world';



Admonition
******************

.. attention::
   this is attention.

.. caution::
   This is caution.

.. danger::
   This is danger.

.. error::
   This is error.

.. hint::
   This is hint.

.. important::
   This is important
   
.. note::
   this is a note text. Use a note for information you want the user to pay particular attention to.

.. seealso::
   this is See also.

.. tip::
   this is tip text.

.. warning::
   This is warning text. Use a warning for information the user must understand to avoid negative consequences.


Glossary
********

Create a glossary
=================

.. glossary::

    Sphinx
      Sphinx is a tool that makes it easy to create intelligent and beautiful documentation. It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages.

    Sublime Text
      Sublime Text is a sophisticated text editor for code, markup and prose. You'll love the slick user interface, extraordinary features and amazing performance.

Link a term to glossary entry
=============================

:term:`Sphinx` 

``:term:`Sphinx```


Sphinx Tutorial 
###############

Figure
******

Figure Number
=============

Figure Numbers are auto generated.

Figue 3a, Figure 3b is not supported.

.. figure:: media/rd002.png
   :name: figure001
   
   figure number is created automatically.

Figure in the list

- item1
  
   .. figure:: media/rd002.png
      :name: figure002
   
      figure example

- item2
  
   - sub item
      .. figure:: media/rd002.png
         :name: figure003

         figure example
   
Figure Reference
================

See :numref:`figure001` ``:numref:`figure001```

See :numref:`figure002` ``:numref:`figure002```  


Table Reference
***************

See :numref:`gridtable` ``:numref:`gridtable```

See :numref:`listtable` ``:numref:`listtable```


Math
****

Basics
======

This is an inline equation embedded :math:`a^2 + b^2 = c^2` in text.

.. code-block::

   This is an inline equation embedded :math:`a^2 + b^2 = c^2` in text.

Equation automatic numbering

.. math:: a^2 + b^2 = c^2
   :label: eq1

.. code-block::

   .. math:: a^2 + b^2 = c^2
      :label: eq1


multi line equation

.. math:: 
  :label: 20_tsg_eq001_01

   \begin{aligned}
      & \mathbf{F}(s)\mathbf{A}(s)=\mathbf{S}(s) \\ 
      & \mathbf{F}(s)=\mathbf{S}(s){{\mathbf{A}}^{-1}}(s) \\ 
   \end{aligned}

.. math:: \begin{aligned}   & \mathbf{F}(s)\mathbf{A}(s)=\mathbf{S}(s) \\    & \mathbf{F}(s)=\mathbf{S}(s){{\mathbf{A}}^{-1}}(s) \\       \end{aligned}
   :label: 20_tsg_eq001_02

.. code-block::

   .. math:: 
   :label: 20_tsg_eq001_01

      \begin{aligned}
         & \mathbf{F}(s)\mathbf{A}(s)=\mathbf{S}(s) \\ 
         & \mathbf{F}(s)=\mathbf{S}(s){{\mathbf{A}}^{-1}}(s) \\ 
      \end{aligned}

   .. math:: \begin{aligned}   & \mathbf{F}(s)\mathbf{A}(s)=\mathbf{S}(s) \\    & \mathbf{F}(s)=\mathbf{S}(s){{\mathbf{A}}^{-1}}(s) \\       \end{aligned}
      :label: 20_tsg_eq001_02

Math in the list
================

.. math::
  :label: listeq1

  a^2 + b^2 = c^2

-  equation1
  
   .. math::
      :label: listeq2

      a^2 + b^2 = c^2

-  equation2

   - nested equation
      .. math::
         :label: listeq3

         a^2 + b^2 = c^2


Equation Number
===============

Use ``:label:`` in math expresstion

.. math::
   :label: myeq_label

   A _i ^j

.. code-block::

   .. math::
      :label: myeq_label

      A _i ^j


Math Reference
==============

See :eq:`myeq_label` ``:eq:`myeq_label```

See :eq:`eq1`

Math Macro
==========

Inline math Using replace
-------------------------

.. |eq0| replace:: :math:`\mathbf{F}(s)`
.. |eq2| replace:: :math:`{{\mathbf{F}}^{-1}}(s)`

|eq0| and |eq2|

.. code-block::

   .. |eq0| replace:: :math:`\mathbf{F}(s)`
   .. |eq2| replace:: :math:`{{\mathbf{F}}^{-1}}(s)`

   ..    |eq0| and and |eq2|


Using mathmacro
---------------

.. |eq12| mathmacro:: \mathbf{A}(s)
.. |eq13| mathmacro:: \mathbf{S}(s)
.. |20_tsg_eq001| mathmacro::    \begin{aligned}   & \mathbf{F}(s)\mathbf{A}(s)=\mathbf{S}(s) \\    & \mathbf{F}(s)=\mathbf{S}(s){{\mathbf{A}}^{-1}}(s) \\       \end{aligned}

|eq12| and |eq13| and |20_tsg_eq001|

.. math:: \eq12 and \eq13
   :label: eq11
   
.. code-block::

   .. |eq12| mathmacro:: \mathbf{A}(s)
   .. |eq13| mathmacro:: \mathbf{S}(s)

   ..    |eq12| and |eq13|

   .. math:: \eq12 and \eq13
      :label: eq11


.. Styled Numbered List
.. ********************

.. With Big Numbers
.. ================

.. .. rst-class:: bignums

.. 1. one

..    Do fist

.. 2. two

..    Do something



Table of Contents Tree
**********************

Section Numbers are auto created.

.. code-block::
   :caption: Table of Content

   .. toctree::
      :numbered:
      :maxdepth: 5

      index
      Tutorial_Sphinx\Tutorial_Sphinx

Themes
******

https://sphinx-themes.org/

40+ themes

shpinx_rtd_theme
================

`Blender <https://docs.blender.org/manual/en/latest/>`_

`fluiddyn <https://fluiddyn.readthedocs.io/en/latest/>`_

`MIT General Circulation Model <https://mitgcm.readthedocs.io/en/latest/overview/overview.html>`_


Custom Theme
============

`Adobe Acrobat <https://www.adobe.com/devnet-docs/acrobatetk/>`_

`Mongo DB <https://docs.mongodb.com/>`_
 
`SciPy <https://docs.scipy.org/doc>`_
 


Output
******

Html (.html)

HtmlHelp (.hhp)

PDF 

ePub

Reference
*********

`Sphinx-doc <https://www.sphinx-doc.org/en/master/>`_ 

`Sphinx-theme <https://sphinx-themes.org/>`_

`Sphinx-rtd-theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/demo/demo.html>`_

`RestructuredText CheatSheet <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_

`Sphinx CheatSheet <https://sphinx-tutorial.readthedocs.io/cheatsheet/>`_

.. `TYPO3 <https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/CheatSheet.html>`__

