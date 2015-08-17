# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
# 2015 CERN.
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

"""Define utilities for special formatting of records."""

import datetime
import time

from flask import current_app, make_response
from flask_login import current_user
from werkzeug.http import http_date

from .api import get_output_format_content_type
from .engine import format_records


def response_formated_records(records, of, **kwargs):
    """Return formatter records.

    Response contains correct Cache and TTL information in HTTP headers.
    """
    response = make_response(format_records(records, of=of, **kwargs))
    response.mimetype = get_output_format_content_type(of)
    current_time = datetime.datetime.now()
    response.headers['Last-Modified'] = http_date(
        time.mktime(current_time.timetuple())
    )
    expires = current_app.config.get(
        'CFG_WEBSEARCH_SEARCH_CACHE_TIMEOUT', None)

    if expires is None:
        response.headers['Cache-Control'] = (
            'no-store, no-cache, must-revalidate, '
            'post-check=0, pre-check=0, max-age=0'
        )
        response.headers['Expires'] = '-1'
    else:
        expires_time = current_time + datetime.timedelta(seconds=expires)
        response.headers['Vary'] = 'Accept'
        response.headers['Cache-Control'] = (
            'public' if current_user.is_guest else 'private'
        )
        response.headers['Expires'] = http_date(time.mktime(
            expires_time.timetuple()
        ))
    return response
