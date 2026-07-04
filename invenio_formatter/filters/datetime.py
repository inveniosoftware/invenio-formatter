# SPDX-FileCopyrightText: 2015-2018 CERN.
# SPDX-License-Identifier: MIT

"""Datetime Jinja filters."""

from warnings import warn

import pendulum
from flask_babel import to_user_timezone


def from_isodate(value, strict=False):
    """Convert an ISO formatted date into a Date object.

    :param value: The ISO formatted date.
    :param strict: If value is falsy, having strict set to ``False`` will
        return ``None``; otherwise parsing will be attempted (default: ``False``).
    :returns: The Date object or ``None``.
    """
    if parsed := from_isodatetime(value, strict=strict):
        return parsed.date()

    return parsed


def from_isodatetime(value, strict=False):
    """Convert an ISO formatted datetime into a DateTime object.

    :param value: The ISO formatted datetime.
    :param strict: If value is falsy, having strict set to ``False`` will
        return ``None``; otherwise parsing will be attempted (default: ``False``).
    :returns: The DateTime object or ``None``.
    """
    if not value and not strict:
        return None

    try:
        if isinstance(value, str):
            return pendulum.parse(value)
        else:
            return to_datetime(value)
    except ValueError as e:
        raise pendulum.parsing.ParserError(e)


def format_datetime(value, format_string):
    """Format a DateTime object.

    :param value: The DateTime object.
    :param format_string: The date format string
    :returns: Returns a string representation of the given DateTime
        object, formatted according to the given format string.

    .. note::
        Do not use this filter to format date/times presented to an end
        user. Instead use ``datetimeformat`` or ``dateformat`` from
        Invenio-I18N.
    """
    assert isinstance(value, pendulum.Date)
    return value.format(format_string)


def to_datetime(value):
    """Convert a Date object to an DateTime object."""
    return pendulum.instance(value)


def naturaltime(value):
    """Get humanized version of time."""
    datetime_obj = to_datetime(value)
    humanized = datetime_obj.diff_for_humans(locale=None)

    return humanized


def to_arrow(value):
    """Deprecated alias for ``to_datetime()``."""
    warnings.warn("Use `to_datetime(value)` instead", DeprecationWarning, stacklevel=2)
    return to_datetime(value)


def format_arrow(value, format_string):
    """Deprecated alias for ``format_datetime()``."""
    warnings.warn(
        "Use `format_datetime(value, format_string)` instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return format_datetime(value, format_string)
