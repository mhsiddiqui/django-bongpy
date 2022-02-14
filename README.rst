django-dynaconf
==================================

Django-dynaconf provides dynamic configuration for your Django project which you can control from Django admin. You can change your configurations at any time without any deployment.

**Note**: You cannot add settings required for Django to operate in this like *INSTALLED_APPS*


Setup
-----

1. Run below command to install.

.. code-block::

    pip install django-dynaconf

2. Add `dynaconf` in your INSTALLED_APPS.
3. Run migration by running following command

.. code-block::

    python manage.py migrate

Usage
_____
Just go to your admin dashboard, in Dynaconf section, add configurations. In your code, you can use it like this.

.. code-block::

    from dynaconf.configs import configs
    print(configs.KEY_OF_YOUR_CONFIGURATION)


At any time, when you will change your config value or add a new value, it will be available to use in you code.
