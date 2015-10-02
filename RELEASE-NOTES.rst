==========================
 Invenio-Formatter v0.2.2
==========================

Invenio-Formatter v0.2.2 was released on October 2, 2015.

About
-----

Invenio module for formatting the bibliographic records.

*This is an experimental development preview release.*

Incompatible changes
--------------------

- Removes legacy upgrade recipes. You **MUST** upgrade to the latest
  Invenio 2.1 before upgrading.

Bug fixes
---------

- Adds missing dependency to pyyaml>=3.11.
- Removes invenio from dependencies and upgrades invenio_base to
  >=0.3.0.
- Removes dependencies to invenio.utils and replaces them with
  invenio_utils.
- Removes calls to PluginManager consider_setuptools_entrypoints()
  removed in PyTest 2.8.0.
- Adds missing invenio_ext dependency and fixes its imports.
- Adds missing `invenio_base` dependency.

Installation
------------

   $ pip install invenio-formatter==0.2.2

Documentation
-------------

   http://invenio-formatter.readthedocs.org/en/v0.2.2

Happy hacking and thanks for flying Invenio-Formatter.

| Invenio Development Team
|   Email: info@invenio-software.org
|   IRC: #invenio on irc.freenode.net
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: https://github.com/inveniosoftware/invenio-formatter
|   URL: http://invenio-software.org
