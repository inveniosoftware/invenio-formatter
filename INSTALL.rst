Installation
============

Invenio-Formatter is on PyPI so all you need is:

.. code-block:: console

   $ pip install invenio-formatter

If you want to use the badge generation feature you need explicit enable it:

.. code-block:: console

   $ pip install invenio-formatter[badges]

This will install `Pillow <https://pypi.python.org/pypi/Pillow>`_ and
`CairoSVG <https://pypi.python.org/pypi/CairoSVG>`_ library. For these
libraries to work you must have the following system libraries installed with
development headers:

- FreeType
- Cairo
- `DejaVu Sans font <http://dejavu-fonts.org/wiki/Main_Page>`_

OS X
~~~~
Install the dependencies above with Homebrew:

.. code-block:: console

   $ brew install cairo

Download the DejaVu Sans font and install it on your system.
