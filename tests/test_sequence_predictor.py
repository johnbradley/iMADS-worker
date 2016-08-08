from unittest import TestCase
from sequence_predictor import PredictionConfig, PredictionCommandGenerator
import yaml

TEST_CONFIG_YAML = """- assembly: hg38
  author_identifier: AA
  cores:
  - GGAA
  - GGAT
  filter_threshold: 0.1
  kmers:
  - 1
  - 2
  - 3
  model_filenames:
  - model1.model
  - model2.model
  protein: ABC1
  serial_number: '9876'
  slope_intercept: false
  track_filename: hg38-9876-ABC1.bb
  width: 20
  transform: False
"""

class PredictionCommandTestCase(TestCase):

  def setUp(self):
    # Load an excerpt of a config from the tracks.yaml data
    self.config_2x2_from_yaml = yaml.load(TEST_CONFIG_YAML)[0]
    self.config_1x3_from_dict = {
              'cores': ['AAAA','CCCC','TTTT'],
              'kmers': [1],
              'model_filenames': ['model'],
              'width': 20,
              }

  def test_parses_config(self):
    pc = PredictionConfig(self.config_2x2_from_yaml)
    self.assertEqual(len(pc.model_filenames), 2)
    self.assertEqual(pc.cores, ['GGAA','GGAT'])
    self.assertEqual(pc.kmers, [1,2,3])

  def test_generates_commands(self):
    pc = PredictionConfig(self.config_2x2_from_yaml)
    pcg = PredictionCommandGenerator(pc, 'sequence.fa', 'output_{}.bed')
    commands = pcg.generate_commands()
    self.assertEqual(len(commands), 2)
    expected_commands = [
      ['predict_tf_binding.py','-S','sequence.fa','-m','model1.model','-c','GGAA','-w','20','-k','1,2,3','-o','output_0.bed',],
      ['predict_tf_binding.py','-S','sequence.fa','-m','model2.model','-c','GGAT','-w','20','-k','1,2,3','-o','output_1.bed',],
    ]
    self.assertEqual(commands, expected_commands)

  def test_generates_single_model_multiple_cores(self):
    pc = PredictionConfig(self.config_1x3_from_dict)
    pcg = PredictionCommandGenerator(pc, 'sequence.fa', 'output_{}.bed')
    commands = pcg.generate_commands()
    self.assertEqual(len(commands), 3)
    expected_commands = [
      ['predict_tf_binding.py','-S','sequence.fa','-m','model','-c','AAAA','-w','20','-k','1','-o','output_0.bed',],
      ['predict_tf_binding.py','-S','sequence.fa','-m','model','-c','CCCC','-w','20','-k','1','-o','output_1.bed',],
      ['predict_tf_binding.py','-S','sequence.fa','-m','model','-c','TTTT','-w','20','-k','1','-o','output_2.bed',],
    ]
    self.assertEqual(commands, expected_commands)

  def test_applies_model_path(self):
    pc = PredictionConfig(self.config_1x3_from_dict)
    pcg = PredictionCommandGenerator(pc, 'sequence.fa', 'output_{}.bed', '/path/to/models/')
    commands = pcg.generate_commands()
    expected_command = ['predict_tf_binding.py','-S','sequence.fa','-m','/path/to/models/model','-c','AAAA','-w','20','-k','1','-o','output_0.bed',]
    self.assertIn(expected_command, commands)



