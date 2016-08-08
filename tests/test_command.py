from unittest import TestCase
from command import PredictionCommandGenerator
from config import PredictionConfig
import test_data

class PredictionCommandTestCase(TestCase):

  def test_generates_commands(self):
    pc = PredictionConfig(test_data.CONFIG_2X2)
    pcg = PredictionCommandGenerator(pc, 'sequence.fa', 'output_{}.bed')
    commands = pcg.generate_commands()
    self.assertEqual(len(commands), 2)
    expected_commands = [
      ['predict_tf_binding.py','-S','sequence.fa','-m','model1.model','-c','GGAA','-w','20','-k','1,2,3','-o','output_0.bed',],
      ['predict_tf_binding.py','-S','sequence.fa','-m','model2.model','-c','GGAT','-w','20','-k','1,2,3','-o','output_1.bed',],
    ]
    self.assertEqual(commands, expected_commands)

  def test_generates_single_model_multiple_cores(self):
    pc = PredictionConfig(test_data.CONFIG_1X3)
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
    pc = PredictionConfig(test_data.CONFIG_1X3)
    pcg = PredictionCommandGenerator(pc, 'sequence.fa', 'output_{}.bed', '/path/to/models/')
    commands = pcg.generate_commands()
    expected_command = ['predict_tf_binding.py','-S','sequence.fa','-m','/path/to/models/model','-c','AAAA','-w','20','-k','1','-o','output_0.bed',]
    self.assertIn(expected_command, commands)



