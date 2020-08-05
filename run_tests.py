#!/usr/bin/env python
import os
import sys 
import tempfile
import django
from django.conf import settings
from django.test.utils import get_runner


if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.unit_tests'
    with tempfile.TemporaryDirectory() as tmp:
        os.environ['OCFL_STORAGE_ROOT'] = tmp
        django.setup()
        TestRunner = get_runner(settings)
        test_runner = TestRunner()
        failures = test_runner.run_tests(['.'])
        sys.exit(bool(failures))

