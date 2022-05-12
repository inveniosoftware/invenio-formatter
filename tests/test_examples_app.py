# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Test example app."""

import datetime
import os
import signal
import subprocess
import time

import pytest


@pytest.yield_fixture
def example_app():
    """Example app fixture."""
    current_dir = os.getcwd()

    # Go to example directory
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    exampleappdir = os.path.join(project_dir, "examples")
    os.chdir(exampleappdir)

    # Start example app
    webapp = subprocess.Popen(
        "FLASK_APP=app.py flask run --debugger -p 5000",
        stdout=subprocess.PIPE,
        preexec_fn=os.setsid,
        shell=True,
    )
    time.sleep(3)
    yield webapp

    # Stop server
    os.killpg(webapp.pid, signal.SIGTERM)

    # Return to the original directory
    os.chdir(current_dir)


def test_example_app(example_app):
    """Test example app."""
    # Testing get index page
    cmd = "curl http://127.0.0.1:5000/"
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")
    expected = (
        '\nToday is {0}\n<img src="/badge/DOI/invenio.12345.svg">'
        "</img>\nInvenio will not be hacked! &lt;a&gt;&lt;/a&gt;.".format(
            datetime.date.today()
        )
    )
    assert expected == output
