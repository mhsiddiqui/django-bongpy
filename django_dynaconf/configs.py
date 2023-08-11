from collections import defaultdict
from django.utils.functional import LazyObject, empty
from django.conf import settings
from .models import Configuration


class Configs(object):
    """
    Class which hold configurations
    """
    CONFIGURATION_COUNT = 0

    def __init__(self, configurations=None):
        self.configure(configurations)

    def configure(self, configurations):
        """
        Configure the Config object by configuration provided
        :param configurations: list/queryset of configuration
        """
        self.CONFIGURATION_COUNT = configurations.count()
        dynaconf_defaults = getattr(settings, 'DYNACONF_DEFAULTS', {})
        for config_key, config_default in dynaconf_defaults.items():
            self.update(config_key, config_default)
        for configuration in configurations:
            self.update(configuration.key, configuration.conf_value)

    def update(self, key, value):
        """
        Update or add configuration
        :param key: configuration key
        :param value: configuration value
        """
        setattr(self, key, value)


class LazyConfigs(LazyObject):
    """
    A lazy proxy for configuration.
    """
    def _setup(self):
        configurations = Configuration.objects.filter(is_active=True)
        self._wrapped = Configs(configurations=configurations)

    def __getattr__(self, name):
        """
        Return the value of a configuration and cache it in self.__dict__.
        """
        if self._wrapped is empty:
            self._setup()
        val = getattr(self._wrapped, name)
        self.__dict__[name] = val
        return val

    def __setattr__(self, name, value):
        """
        Set the value of configuration. Clear all cached values if _wrapped changes
        """
        if name == '_wrapped':
            self.__dict__.clear()
        else:
            self.__dict__.pop(name, None)
        super(LazyConfigs, self).__setattr__(name, value)

    def __delattr__(self, name):
        """
        Delete a configuration and clear it from cache if needed.
        """
        super(LazyConfigs, self).__delattr__(name)
        self.__dict__.pop(name, None)

    def configure(self, configuration):
        """
        Configure a configuration
        :param configuration: a config object
        """
        if self._wrapped is not empty:
            configs_obj = self._wrapped
            configs_obj.update(configuration.key, configuration.conf_value)
            self._wrapped = configs_obj
        else:
            self._setup()

    @property
    def configured(self):
        """
        Returns True if the configuration have already been configured.
        """
        return self._wrapped is not empty

    def grouped(self, group):
        """
        Return grouped configurations
        """
        configurations = Configuration.objects.filter(group=group, is_active=True)
        if configurations.exists():
            return Configs(configurations=configurations)
        return empty


configs = LazyConfigs()
