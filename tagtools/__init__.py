from __future__ import absolute_import

from tagtools.tagcloud import *
from tagtools.settings import *

def get_tagcloud_for_model(model, steps=CLOUD_STEPS, min_count=CLOUD_MIN_COUNT):
    raise NotImplemented, "No tag-app found"

def set_tags_for_model(tags, model):
    raise NotImplemented, "No tag-app found"

if PREFERRED_APP_ORDER and not TAG_APP:
    taggit = None
    tagging = None
    _tag_app_map = {}
    if 'taggit' in PREFERRED_APP_ORDER:
        from tagtools.backends import taggit
        _tag_app_map['taggit'] = taggit.get_tagcloud_for_model
    if 'tagging' in PREFERRED_APP_ORDER:
        from tagtools.backends import tagging
        _tag_app_map['tagging'] = tagging.get_tagcloud_for_model

    def _generic_get_tagcloud_for_model(model, steps=CLOUD_STEPS, min_count=CLOUD_MIN_COUNT):
        for app in PREFERRED_APP_ORDER:
            return _tag_app_map[app](model, steps, min_count)
        return ()

    def _generic_set_tags_for_model(tags, model):
        if getattr(model.tags, '__module__', False):
            return taggit.set_tags_for_model(tags, model)
        return model, None

if TAG_APP == 'taggit':
    from tagtools.backends.taggit import *
elif TAG_APP == 'tagging':
    from tagtools.backends.tagging import *
elif not TAG_APP:
    if PREFERRED_APP_ORDER:
        get_tagcloud_for_model = _generic_get_tagcloud_for_model
        set_tags_for_model = _generic_set_tags_for_model
