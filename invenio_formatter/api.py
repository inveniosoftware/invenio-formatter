# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Formatter API."""

from . import registry


# Output formats related functions
def get_format_by_code(code):
    """
    Returns the output format object given by code in the database.

    Output formats are located inside 'format' table

    :param code: the code of an output format
    :return: Format object with given ID. None if not found
    """
    f_code = code
    if len(code) > 6:
        f_code = code[:6]
    return registry.output_formats.get(f_code.lower(), {})


def get_format_property(code, property_name, default_value=None):
    """
    Returns the value of a property of the output format given by code.

    If code or property does not exist, return default_value

    :param code: the code of the output format to get the value from
    :param property_name: name of property to return
    :param default_value: value to be returned if format not found
    :return: output format property value
    """
    return get_format_by_code(code).get(property_name, default_value)


def get_output_format_description(code):
    """
    Returns the description of the output format given by code

    If code or description does not exist, return empty string

    :param code: the code of the output format to get the description from
    :return: output format description
    """
    return get_format_property(code, 'description', '')


def get_output_format_visibility(code):
    """
    Returns the visibility of the output format, given by its code

    If code does not exist, return 0

    :param code: the code of an output format
    :return: output format visibility (0 if not visible, 1 if visible
    """
    visibility = get_format_property(code, 'visibility', 0)

    if visibility is not None and int(visibility) in range(0, 2):
        return int(visibility)
    else:
        return 0


def get_output_format_content_type(code, default_content_type='text/html'):
    """
    Returns the content_type of the output format given by code

    If code or content_type does not exist, return empty string

    :param code: the code of the output format to get the description from
    :return: output format content_type
    """
    return get_format_property(code, 'content_type', default_content_type) or \
        default_content_type
