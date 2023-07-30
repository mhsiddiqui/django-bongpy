from django.core.exceptions import ValidationError
from django.test import TestCase

from django_dynaconf.configs import configs
from django_dynaconf.models import FALSE_VALUES, TRUE_VALUES, Configuration


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

    GROUP_1_KEY_1 = {
        'key': 'GROUP_1_KEY_1',
        'group': 'G1',
        'value': 'value',
        'type': Configuration.STRING
    }

    GROUP_1_KEY_2 = {
        'key': 'GROUP_1_KEY_2',
        'group': 'G1',
        'value': '2',
        'type': Configuration.NUMBER
    }

    GROUP_2_KEY_1 = {
        'key': 'GROUP_2_KEY_1',
        'group': 'G2',
        'value': 'True',
        'type': Configuration.BOOLEAN
    }

    GROUP_2_KEY_2 = {
        'key': 'GROUP_2_KEY_2',
        'group': 'G2',
        'value': 'string',
        'type': Configuration.STRING
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

    def test_grouped_config(self):
        group_1_key_1 = Configuration.objects.create(**TestData.GROUP_1_KEY_1)
        group_1_key_2 = Configuration.objects.create(**TestData.GROUP_1_KEY_2)
        Configuration.objects.create(**TestData.GROUP_2_KEY_1)
        Configuration.objects.create(**TestData.GROUP_2_KEY_2)
        # Check g1 configs
        g1_configs = configs.grouped(group=TestData.GROUP_1_KEY_1.get('group'))
        self.assertTrue(hasattr(g1_configs, TestData.GROUP_1_KEY_1.get('key')))
        self.assertTrue(hasattr(g1_configs, TestData.GROUP_1_KEY_2.get('key')))
        self.assertTrue(not hasattr(g1_configs, TestData.GROUP_2_KEY_1.get('key')))
        self.assertTrue(not hasattr(g1_configs, TestData.GROUP_2_KEY_2.get('key')))

        self.assertEqual(
            getattr(g1_configs, TestData.GROUP_1_KEY_1.get('key')), group_1_key_1.conf_value
        )
        self.assertEqual(
            getattr(g1_configs, TestData.GROUP_1_KEY_2.get('key')), group_1_key_2.conf_value
        )
