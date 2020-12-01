#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

set -o errexit 

set -o nounset 

pydocstyle invenio_formatter tests docs
python -m check_manifest --ignore ".*-requirements.txt"
isort invenio_formatter tests --check-only --diff
sphinx-build -qnNW docs docs/_build/html
python setup.py test
sphinx-build -qnNW -b doctest docs docs/_build/doctest
