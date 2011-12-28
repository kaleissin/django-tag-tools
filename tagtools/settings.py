from django.conf import settings

_DEFAULT_APP_ORDER = ('taggit', 'tagging')
_DEFAULT_CLOUD_STEPS = 6
_DEFAULT_CLOUD_MIN_COUNT = 1

PREFERRED_APP_ORDER = getattr(settings, 'TAGTOOLS_PREFERRED_APP_ORDER', _DEFAULT_APP_ORDER)
TAG_APP = getattr(settings, 'TAGTOOLS_TAG_APP', None)
CLOUD_STEPS = getattr(settings, 'TAGTOOLS_CLOUD_STEPS', _DEFAULT_CLOUD_STEPS)
CLOUD_MIN_COUNT = getattr(settings, 'TAGTOOLS_CLOUD_MIN_COUNT', _DEFAULT_CLOUD_MIN_COUNT)

if not TAG_APP in _DEFAULT_APP_ORDER:
    TAG_APP = None
else:
    try:
        if TAG_APP == 'taggit':
            import taggit
        if TAG_APP == 'tagging': 
            import tagging
    except ImportError:
        TAG_APP = None
