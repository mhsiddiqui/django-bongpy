import django

__version__ = '1.3.1'

if django.VERSION < (3, 2):  # pragma: no cover
    default_app_config = 'django_dynaconf.apps.DjangoDynaconfConfig'
