from unittest import TestCase
from cwljob import CwlJobGenerator
import test_data
import tempfile

class CwlJobGeneratorTestCase(TestCase):

  def tests_model_dict(self):
    g = CwlJobGenerator(test_data.CONFIG_2X2)
    self.assertIsNotNone(g.job)
    self.assertNotIn('models', test_data.CONFIG_2X2, 'test dataset should have model_filenames')
    self.assertIn('models', g.job, 'generated job dict should just have models')

  def test_writes_json(self):
    g = CwlJobGenerator(test_data.CONFIG_2X2)
    output_file = tempfile.NamedTemporaryFile()
    self.assertEqual(output_file.tell(), 0)
    g.write_json(output_file)
    self.assertNotEqual(output_file.tell(), 0, 'write_json should have written to the file')

  def test_matrixes_models(self):
    g = CwlJobGenerator(test_data.CONFIG_1X3)
    self.assertEqual(len(test_data.CONFIG_1X3['model_filenames']), 1)
    self.assertEqual(len(test_data.CONFIG_1X3['cores']), 3)
    self.assertEqual(len(g.job['models']), 3)
    self.assertEqual(len(g.job['cores']), 3)
