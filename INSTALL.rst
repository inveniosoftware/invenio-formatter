..
    This file is part of Invenio.
    Copyright (C) 2015-2018 CERN.

    Invenio is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

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
- `DejaVu Sans font <https://dejavu-fonts.github.io>`_

Linux
~~~~~
Install the dependencies with your package manager. For Ubuntu or Debian:

.. code-block:: console

   $ sudo apt-get install libcairo2-dev

OS X
~~~~
Install the dependencies above with Homebrew:

.. code-block:: console

   $ brew install cairo

Download the [DejaVu Sans](https://dejavu-fonts.github.io) font and install it on your system.

.. code-block:: console

    $ brew install homebrew/cask-fonts/font-dejavu-sans
