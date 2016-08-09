from unittest import TestCase
from cwljob import CwlJobGenerator
import test_data

class CwlJobGeneratorTestCase(TestCase):

  def tests_model_dict(self):
    g = CwlJobGenerator(test_data.CONFIG_2X2)
    j = g.generate_job()
    self.assertIsNotNone(j)
    self.assertNotIn('models', test_data.CONFIG_2X2, 'test dataset should have model_filenames')
    self.assertIn('models', j, 'generated job dict should just have models')
