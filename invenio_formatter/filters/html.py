# SPDX-FileCopyrightText: 2019 CERN.
# SPDX-License-Identifier: MIT

"""HTML sanitisation Jinja filters."""

import bleach
from flask import current_app


def sanitize_html(value, tags=None, attributes=None):
    """Sanitize HTML.

    :param tags: Allowed HTML ``tags``. Configuration set by Invenio-Config.
    :param attributes: Allowed HTML ``attributes``. Configuration set by
        Invenio-Config.

    Use this function when you need to include unescaped HTML that contain
    user provided data.
    """
    return bleach.clean(
        value,
        tags=tags or current_app.config.get("ALLOWED_HTML_TAGS", []),
        attributes=attributes or current_app.config.get("ALLOWED_HTML_ATTRS", {}),
        strip=True,
    ).strip()
