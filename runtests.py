import sys

from django.conf import settings

sys.path.append('.')

APP = 'tagtools'

settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'taggit',
        'tagging',
        APP,
    )
)

# MUST be imported *after* settings.configure() has run!
from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests([APP,])
if failures:
    sys.exit(failures)
