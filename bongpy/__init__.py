import django

__version__ = '1.4'

if django.VERSION < (3, 2):  # pragma: no cover
    default_app_config = 'bongpy.apps.BongPyConfig'
