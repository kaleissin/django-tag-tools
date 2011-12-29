from django.db.models.loading import cache as app_cache, ImproperlyConfigured
from django.conf import settings

_DEFAULT_APP_ORDER = ('taggit', 'tagging')
_DEFAULT_CLOUD_STEPS = 6
_DEFAULT_CLOUD_MIN_COUNT = 1

PREFERRED_APP_ORDER = getattr(settings, 'TAGTOOLS_PREFERRED_APP_ORDER', _DEFAULT_APP_ORDER)
TAG_APP = getattr(settings, 'TAGTOOLS_TAG_APP', None)
CLOUD_STEPS = getattr(settings, 'TAGTOOLS_CLOUD_STEPS', _DEFAULT_CLOUD_STEPS)
CLOUD_MIN_COUNT = getattr(settings, 'TAGTOOLS_CLOUD_MIN_COUNT', _DEFAULT_CLOUD_MIN_COUNT)

def _set_tag_app():
    apps = []
    for app in PREFERRED_APP_ORDER:
        try:
            app_cache.get_app(app)
            apps.append(app)
        except ImproperlyConfigured:
            pass
    return apps

PREFERRED_APP_ORDER = _set_tag_app()

if not TAG_APP in PREFERRED_APP_ORDER:
    TAG_APP = None
