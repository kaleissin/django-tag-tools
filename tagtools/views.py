from __future__ import absolute_import

from tagtools.settings import *

if TAG_APP == 'taggit':
    from tagtools.backends.taggit.views import tagged_object_list
elif TAG_APP == 'tagging':
    from tagtools.backends.tagging.views import tagged_object_list
else:
    def tagged_object_list(*args, **kwargs):
        raise NotImplementedError, 'No tag-app found, set to: %s' % TAG_APP
