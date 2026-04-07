from __future__ import absolute_import, division, print_function

import io

from django.core.management import call_command


def test_no_migrations_required(db):
    stdout = io.StringIO()
    call_command('makemigrations', 'gargoyle', stdout=stdout)
    assert stdout.getvalue() == "No changes detected in app 'gargoyle'\n"
