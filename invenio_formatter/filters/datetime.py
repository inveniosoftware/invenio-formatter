# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016, 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Datetime Jinja filters."""

from __future__ import absolute_import, print_function

import arrow


def from_isodate(value, strict=False):
    """Convert an ISO formatted date into a Date object.

    :param value: The ISO formatted date.
    :param strict: If value is ``None``, then if strict is ``True`` it returns
        the Date object of today, otherwise it returns ``None``.
        (Default: ``False``)
    :returns: The Date object or ``None``.
    """
    if value or strict:
        return arrow.get(value).date()


def from_isodatetime(value, strict=False):
    """Convert an ISO formatted datetime into a Date object.

    :param value: The ISO formatted datetime.
    :param strict: If value is ``None``, then if strict is ``True`` it returns
        the Date object of today, otherwise it returns ``None``.
        (Default: ``False``)
    :returns: The Date object or ``None``.
    """
    if value or strict:
        return arrow.get(value).datetime


def format_arrow(value, format_string):
    """Format an arrow datetime object.

    :param value: The arrow datetime object.
    :param format_string: The date format string
    :returns: Returns a string representation of the given arrow datetime
        object, formatted according to the given format string.

    .. note::
        Do not use this filter to format date/times presented to an end
        user. Instead use ``datetimeformat`` or ``dateformat`` from
        Invenio-I18N.
    """
    assert isinstance(value, arrow.Arrow)
    return value.format(format_string)


def to_arrow(value):
    """Convert a Date object to an arrow datetime object."""
    return arrow.get(value)
