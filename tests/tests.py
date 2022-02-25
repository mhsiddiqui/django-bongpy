from django.core.exceptions import ValidationError
from django.test import TestCase
from dynaconf.configs import configs
from dynaconf.models import Configuration, TRUE_VALUES, FALSE_VALUES


class TestData(object):
    VALID_STRING = {
        'key': 'TEST_VALID_STRING_KEY',
        'value': 'Test Config Value'
    }

    VALID_INT = {
        'key': 'TEST_VALID_INT_KEY',
        'value': '1',
        'type': Configuration.NUMBER
    }

    INVALID_INT = {
        'key': 'TEST_INVALID_INT_KEY',
        'value': 'invalid integer',
        'type': Configuration.NUMBER
    }

    VALID_DECIMAL = {
        'key': 'TEST_VALID_DECIMAL_KEY',
        'value': '1.122',
        'type': Configuration.NUMBER
    }

    INVALID_DECIMAL = {
        'key': 'TEST_INVALID_DECIMAL_KEY',
        'value': 'invalid decimal',
        'type': Configuration.NUMBER
    }

    BOOLEAN = {
        'key': 'TEST_BOOLEAN_KEY',
        'type': Configuration.BOOLEAN
    }

    VALID_JSON = {
        'key': 'TEST_VALID_JSON_KEY',
        'value': '{"a": 1, "b": 2}',
        'type': Configuration.JSON
    }

    INVALID_JSON = {
        'key': 'TEST_INVALID_JSON_KEY',
        'value': 'invalid json',
        'type': Configuration.JSON
    }

    VALID_DATE = {
        'key': 'TEST_VALID_DATE_KEY',
        'value': '2020-09-12',
        'type': Configuration.DATE
    }

    INVALID_DATE = {
        'key': 'TEST_INVALID_DATE_KEY',
        'value': '2020-09-2020',
        'type': Configuration.DATE
    }

    VALID_DATETIME = {
        'key': 'TEST_VALID_DATETIME_KEY',
        'value': '2020-09-12 10:50:12',
        'type': Configuration.DATETIME
    }

    INVALID_DATETIME = {
        'key': 'TEST_INVALID_DATETIME_KEY',
        'value': '2020-09-2022 10:50:12',
        'type': Configuration.DATETIME
    }

    VALID_TIME = {
        'key': 'TEST_VALID_TIME_KEY',
        'value': '10:50:12',
        'type': Configuration.DATE
    }

    INVALID_TIME = {
        'key': 'TEST_INVALID_TIME_KEY',
        'value': 'invalid time',
        'type': Configuration.DATE
    }


class DynaConfTests(TestCase):
    def test_valid_creating_string_config(self):
        config = Configuration.objects.create(**TestData.VALID_STRING)
        self.assertEqual(
            getattr(configs, TestData.VALID_STRING.get('key')),
            config.conf_value, 'Config values are not equal'
        )

    def test_valid_integer_config(self):
        config = Configuration.objects.create(**TestData.VALID_INT)
        self.assertEqual(
            getattr(configs, TestData.VALID_INT.get('key')),
            config.conf_value, 'Config values are not equal'
        )

    def test_invalid_integer_config(self):
        try:
            Configuration.objects.create(**TestData.INVALID_INT)
            self.assertTrue(False, 'Added invalid config value')
        except ValidationError:
            self.assertTrue(True)

    def test_valid_decimal_config(self):
        config = Configuration.objects.create(**TestData.VALID_DECIMAL)
        self.assertEqual(
            getattr(configs, TestData.VALID_DECIMAL.get('key')),
            config.conf_value, 'Config values are not equal'
        )

    def test_invalid_decimal_config(self):
        try:
            Configuration.objects.create(**TestData.INVALID_DECIMAL)
            self.assertTrue(False, 'Added invalid config value')
        except ValidationError:
            self.assertTrue(True)

    def test_valid_boolean_config(self):
        config = Configuration.objects.create(**TestData.VALID_DECIMAL)
        self.assertEqual(
            getattr(configs, TestData.VALID_DECIMAL.get('key')),
            config.conf_value, 'Config values are not equal'
        )

    def test_boolean_config(self):
        config_data = TestData.BOOLEAN
        for config_value in (list(TRUE_VALUES) + list(FALSE_VALUES)):
            config_data['value'] = config_value
            config = Configuration.objects.create(**config_data)
            self.assertEqual(
                getattr(configs, config_data.get('key')),
                config.conf_value, 'Config values are not equal'
            )
            config.delete()

    def test_valid_json_config(self):
        config = Configuration.objects.create(**TestData.VALID_JSON)
        self.assertEqual(
            getattr(configs, TestData.VALID_JSON.get('key')),
            config.conf_value, 'Config values are not equal'
        )

    def test_invalid_json_config(self):
        try:
            Configuration.objects.create(**TestData.INVALID_JSON)
            self.assertTrue(False, 'Added invalid config value')
        except ValidationError:
            self.assertTrue(True)

    def test_valid_date_config(self):
        config = Configuration.objects.create(**TestData.VALID_DATE)
        self.assertEqual(
            getattr(configs, TestData.VALID_DATE.get('key')),
            config.conf_value, 'Config values are not equal'
        )

    def test_invalid_date_config(self):
        try:
            Configuration.objects.create(**TestData.INVALID_DATE)
            self.assertTrue(False, 'Added invalid config value')
        except ValidationError:
            self.assertTrue(True)

    def test_valid_datetime_config(self):
        config = Configuration.objects.create(**TestData.VALID_DATETIME)
        self.assertEqual(
            getattr(configs, TestData.VALID_DATETIME.get('key')),
            config.conf_value, 'Config values are not equal'
        )

    def test_invalid_datetime_config(self):
        try:
            Configuration.objects.create(**TestData.INVALID_DATETIME)
            self.assertTrue(False, 'Added invalid config value')
        except ValidationError:
            self.assertTrue(True)

    def test_valid_time_config(self):
        config = Configuration.objects.create(**TestData.VALID_TIME)
        self.assertEqual(
            getattr(configs, TestData.VALID_TIME.get('key')),
            config.conf_value, 'Config values are not equal'
        )

    def test_invalid_time_config(self):
        try:
            Configuration.objects.create(**TestData.INVALID_TIME)
            self.assertTrue(False, 'Added invalid config value')
        except ValidationError:
            self.assertTrue(True)
