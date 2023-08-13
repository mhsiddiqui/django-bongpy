import json

from django.utils.functional import LazyObject, empty
from django.conf import settings
from .models import Configuration, get_configuration_type


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
        self.init()

    @property
    def active_configurations(self):
        """
        Return active configurations
        """
        return Configuration.objects.filter(is_active=True)

    def load_initial_data(self):
        """
        Load data from defaults
        """
        defaults = getattr(settings, 'BONGPY_DEFAULTS', {})
        existing_keys = set(
            Configuration.objects.filter(key__in=defaults.keys()).values_list('key', flat=True)
        )
        configurations = []
        for key, value in defaults.items():
            if key not in existing_keys:
                conf_type = get_configuration_type(value)
                if conf_type == Configuration.JSON:
                    value = json.dumps(value)
                else:
                    value = str(value)
                configurations.append(Configuration(
                    key=key, value=value, type=conf_type
                ))
        Configuration.objects.bulk_create(configurations)

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

    def init(self):
        """
        Initialize cpnfig object. This can be used to refresh configurations
        """
        self.load_initial_data()
        self._wrapped = Configs(configurations=self.active_configurations)

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
