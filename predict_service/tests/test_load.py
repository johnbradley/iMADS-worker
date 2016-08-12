from unittest import TestCase

from load import ConfigLoader


class CwlJobGeneratorTestCase(TestCase):
    def test_loads_configs(self):
        metadata_file_name = 'tests/test_config.yaml'
        model_id = 'LLLL_5555(CD)'
        c = ConfigLoader(model_id, metadata_file_name)
        config = c.config
        self.assertIsNotNone(config)
        self.assertEqual(config['model_filenames'], ['model_5555.model'])

    def test_fails_without_data(self):
        with self.assertRaises(ValueError):
            ConfigLoader('model', None)
        with self.assertRaises(ValueError):
            ConfigLoader(None, 'filename.yaml')
