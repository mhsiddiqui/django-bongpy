import json
import re
from ast import literal_eval

import django
from dateutil.parser import ParserError, parse
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.dispatch import receiver

if django.VERSION < (3, 0):
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _

INVALID_VALUE_FOR_TYPE = _('Invalid value for type {type}')
DATE_SHOULD_BE_IN_FORMAT = _('Date should be in YYYY-MM-DD format')
DATETIME_SHOULD_BE_IN_FORMAT = _('Datetime should be in "YYYY-MM-DD HH:MM:SS" format')
TIME_SHOULD_BE_IN_FORMAT = _('Time should be in HH:MM:SS format')


TRUE_VALUES = {
    't', 'T',
    'y', 'Y', 'yes', 'YES',
    'true', 'True', 'TRUE',
    'on', 'On', 'ON',
    '1', 1,
    True
}
FALSE_VALUES = {
    'f', 'F',
    'n', 'N', 'no', 'NO',
    'false', 'False', 'FALSE',
    'off', 'Off', 'OFF',
    '0', 0, 0.0,
    False
}


class Configuration(models.Model):
    """
    Configuration model
    """
    STRING = 'string'
    NUMBER = 'number'
    BOOLEAN = 'boolean'
    JSON = 'json'
    DATE = 'date'
    DATETIME = 'datetime'
    TIME = 'time'
    DEFAULT_GROUP = 'DEFAULT'
    VALUE_TYPE = (
        (STRING, _('String')),
        (NUMBER, _('Number')),
        (BOOLEAN, _('Boolean')),
        (JSON, _('Json')),
        (DATE, _('Date')),
        (DATETIME, _('Datetime')),
        (TIME, _('Time')),
    )
    key = models.CharField(max_length=100, unique=True, validators=[
        RegexValidator(
            regex=r"[A-Z\d_]+",
            message=_('Key can only contains uppercase letters, numbers and _')
        )
    ])
    group = models.CharField(
        max_length=100, default=DEFAULT_GROUP, validators=[
            RegexValidator(
                regex=r"[A-Z\d_]+",
                message=_('Group can only contains uppercase letters, numbers and _')
            )
        ]
    )
    description = models.CharField(
        max_length=200, null=True, blank=True, help_text=_('Description of configuration')
    )
    value = models.TextField()
    type = models.CharField(choices=VALUE_TYPE, max_length=20, default=STRING)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.clean()
        return super(Configuration, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.key

    def clean(self):
        if self.type == self.NUMBER:
            self.clean_number()
        elif self.type == self.BOOLEAN:
            self.clean_boolean()
        elif self.type == self.JSON:
            self.clean_json()
        elif self.type == self.TIME:
            self.clean_time()
        elif self.type == self.DATE:
            self.clean_date()
        elif self.type == self.DATETIME:
            self.clean_datetime()

    def clean_number(self):
        if not re.match(r"-?\d*\.?\d+", self.value):
            raise ValidationError(INVALID_VALUE_FOR_TYPE.format(type='number'))

    def clean_boolean(self):
        if self.value not in TRUE_VALUES and self.value not in FALSE_VALUES:
            raise ValidationError(INVALID_VALUE_FOR_TYPE.format(type='boolean'))

    def clean_json(self):
        try:
            json.loads(self.value)
        except ValueError:
            raise ValidationError(INVALID_VALUE_FOR_TYPE.format(type='json'))

    def clean_date(self):
        try:
            parse(self.value)
        except ParserError:
            raise ValidationError(DATE_SHOULD_BE_IN_FORMAT)

    def clean_datetime(self):
        try:
            parse(self.value)
        except ParserError:
            raise ValidationError(DATETIME_SHOULD_BE_IN_FORMAT)

    def clean_time(self):
        try:
            parse(self.value)
        except ParserError:
            raise ValidationError(TIME_SHOULD_BE_IN_FORMAT)

    @property
    def conf_value(self):
        if self.type == self.NUMBER:
            return literal_eval(self.value)
        elif self.type == self.BOOLEAN:
            if self.value in TRUE_VALUES:
                return True
            elif self.value in FALSE_VALUES:
                return False
        elif self.type == self.JSON:
            return json.loads(self.value)
        elif self.type == self.TIME:
            return parse(self.value).time()
        elif self.type == self.DATE:
            return parse(self.value).date()
        elif self.type == self.DATETIME:
            return parse(self.value)
        return self.value


@receiver(signal=models.signals.post_save, sender=Configuration)
def update_config_object(sender, instance, created, **kwarg):
    """
    Update config object if a new object is added or already added object changes
    """
    from .configs import configs
    configs.configure(instance)
