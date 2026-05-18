# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""Configuration for Invenio-Formatter."""

FORMATTER_BADGES_ALLOWED_TITLES = ["DOI"]
"""List of allowed titles in badges."""

FORMATTER_BADGES_TITLE_MAPPING = {}
"""Mapping of titles."""

FORMATTER_BADGES_MAX_CACHE_AGE = 0
"""The maximum amount of time a badge will be considered fresh."""

FORMATTER_BADGES_DENY_CACHING = True
"""Set response header fields to prevent caching of generated badges."""
