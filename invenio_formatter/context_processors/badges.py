# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Badges context processor."""

from __future__ import absolute_import, print_function

from base64 import b64encode

import cairosvg
from PIL import Image, ImageDraw, ImageFont


def get_text_length(*args):
    r"""Measure the size of string rendered with a TTF no-nomospaced fonts.

    :param \*args: List of strings to be measured.
    :returns: The length of the strings.
    """
    txt = Image.new("RGBA", (16, 16), (255, 255, 255, 0))
    d = ImageDraw.Draw(txt)
    font = ImageFont.truetype("DejaVuSans", 11)
    result = ()
    for value in args:
        result = result + (d.textsize(value, font=font)[0],)
    return result


def generate_badge_svg(title, value, color="#007ec6"):
    """Generate the SVG.

    :param title: The badge title.
    :param value: The badge content.
    :param color: The badge color. (Default: ``'#007ec6'``)
    :returns: The SVG badge.
    """
    (title_length, value_length) = get_text_length(title, value)
    return """<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}" height="20">
        <linearGradient id="b" x2="0" y2="100%">
            <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
            <stop offset="1" stop-opacity=".1"/>
        </linearGradient>
        <mask id="a" width="{width}" height="20">
            <rect width="{width}" height="20" rx="3"
            fill="#fff"/>
        </mask>
        <g mask="url(#a)">
            <path fill="#555" d="M0 0h{title_width}v20H0z" />
            <path fill="{color}"
            d="M{title_width} 0h{value_width}v20H{title_width}z"
            />
            <path fill="url(#b)" d="M0 0h{width}v20H0z" />
        </g>
        <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,
        Verdana,Geneva,sans-serif" font-size="11">
            <text x="{title_position}" y="15" fill="#010101"
            fill-opacity=".3">
                {title}
            </text>
            <text x="{title_position}" y="14">
                {title}
            </text>
            <text x="{value_position}"
            y="15" fill="#010101" fill-opacity=".3">
                {value}
            </text>
            <text x="{value_position}" y="14">
                {value}
            </text>
        </g>
    </svg>""".format(
        title_width=title_length + 11,
        value_width=value_length + 11,
        width=title_length + value_length + 22,
        title_position=title_length / 2 + 6,
        value_position=title_length + value_length / 2 + 16,
        title=title,
        value=value,
        color=color,
    )


def generate_badge_png(title, value, color="#007ec6"):
    """Generate the badge in PNG format."""
    badge = generate_badge_svg(title, value, color)
    return cairosvg.svg2png(badge)


def badges_processor():
    """Context processor for badges."""

    def badge_svg(title, value, color="#007ec6"):
        """Context processor function to generate SVG badges."""
        return generate_badge_svg(title, value, color)

    def badge_png(title, value, color="#007ec6"):
        """Context processor function to generate SVG badges."""
        png = generate_badge_png(title, value, color)
        png_base64 = b64encode(png)
        return "data:image/png;base64,{0}".format(png_base64)

    return dict(badge_svg=badge_svg, badge_png=badge_png)
