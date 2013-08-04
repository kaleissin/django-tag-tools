=========
Tag tools
=========

This currently provides a tag cloud generator for django-tagging and
django-taggit.

Optional settings
-----------------

TAGTOOLS_PREFERRED_APP_ORDER
    If TAGTOOLS_TAG_APP is not set, it will attempt to import the
    tag-apps in the order defined here. **Default:** ('taggit', 'tagging')

TAGTOOLS_TAG_APP
    Force what app to use. **Default:** pick first found entry in
    TAGTOOLS_PREFERRED_APP_ORDER

TAGTOOLS_CLOUD_STEPS
    How many different sizes of tags for the cloud. **Default:** 6

TAGTOOLS_CLOUD_MIN_COUNT
    Minimum frequency of a tag before it is included. **Default:** 1

Usage
-----

There's a view ``tagged_object_list`` if you want to devote an entire
page to a tag-cloud. In your url-conf:

    tags_dict= {
            'queryset_or_model': YorTaggedModel,
            'template_name': 'sometemplate.html',
            }
    
    urlpatterns = patterns('tagtools.views',
        (r'^tag/(?P<tag>[-\w\d]+)/$', 'tagged_object_list', tags_dict),
    )

You can generate lists of tags in a view with the function
``tagtools.get_tagcloud_for_model``.

You can set tags for a model with ``tagtools.set_tags_for_model``.


:Version: 0.1
