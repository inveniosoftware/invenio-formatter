# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Configuration for Invenio-Formatter."""

from __future__ import absolute_import, print_function

FORMATTER_BADGES_ALLOWED_TITLES = ["DOI"]
"""List of allowed titles in badges."""

FORMATTER_BADGES_TITLE_MAPPING = {}
"""Mapping of titles."""

FORMATTER_BADGES_MAX_CACHE_AGE = 0
"""The maximum amount of time a badge will be considered fresh."""
