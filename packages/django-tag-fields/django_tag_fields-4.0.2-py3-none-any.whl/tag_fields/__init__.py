try:
    import django
except ImportError:
    # setup.py and docs do not have Django installed.
    django = None

# VERSION = (4, 0, 0)
__version__ = "4.0.2"

if django and django.VERSION < (3, 2):
    default_app_config = "tag_fields.apps.TaggitAppConfig"
