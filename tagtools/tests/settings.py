SECRET_KEY = 'xt@clh!4b%-xk#ipm@__98(97k%y10&4prv7q6ts@4vi1^)99w'

DATABASES={
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
    }
}

INSTALLED_APPS=(
    'django.contrib.contenttypes',
    'taggit',
    'tagtools',
    'tagtools.tests',
)

MIDDLEWARE_CLASSES=()

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
