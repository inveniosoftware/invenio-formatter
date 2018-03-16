Changes
=======

Version 1.0.0b3 (released 2017-06-02)
-------------------------------------

Incompatible changes
~~~~~~~~~~~~~~~~~~~~

- Major refactoring.


Version 0.2.2 (released 2015-10-02)
-----------------------------------

Incompatible changes
~~~~~~~~~~~~~~~~~~~~

- Removes legacy upgrade recipes. You **MUST** upgrade to the latest
  Invenio 2.1 before upgrading.

Bug fixes
~~~~~~~~~

- Adds missing dependency to pyyaml>=3.11.
- Removes invenio from dependencies and upgrades invenio_base to
  >=0.3.0.
- Removes dependencies to invenio.utils and replaces them with
  invenio_utils.
- Removes calls to PluginManager consider_setuptools_entrypoints()
  removed in PyTest 2.8.0.
- Adds missing invenio_ext dependency and fixes its imports.
- Adds missing `invenio_base` dependency.

Version 0.2.1 (released 2015-08-25)
-----------------------------------

- Adds missing `invenio_upgrader` dependency following its separation
  into standalone package.
- Fixes import of invenio_upgrader.

Version 0.2.0 (released 2015-08-17)
-----------------------------------

- Removes unused legacy functions.  (#3)
- Ports `response_formated_records` from Invenio search module.

Version 0.1.0 (released 2015-08-12)
-----------------------------------
