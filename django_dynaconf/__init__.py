import django

__version__ = '1.2'

if django.VERSION < (3, 2):  # pragma: no cover
    default_app_config = 'django_dynaconf.apps.DjangoDynaconfConfig'
