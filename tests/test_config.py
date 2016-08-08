from unittest import TestCase
from config import PredictionConfig
import test_data

class PredictionConfigTestCase(TestCase):

  def test_parses_config(self):
    pc = PredictionConfig(test_data.CONFIG_2X2)
    self.assertEqual(len(pc.model_filenames), 2)
    self.assertEqual(pc.cores, ['GGAA','GGAT'])
    self.assertEqual(pc.kmers, [1,2,3])
