from runner import PredictionRunner, ConfigNotFoundException
from unittest import TestCase
import tempfile
import shutil

class PredictionRunnerTestCase(TestCase):
  sequence = 'tests/test_sequence.fa'
  model = 'ABCD_1234(AB)'
  config = 'tests/test_config.yaml'
  workflow = 'tests/test_workflow.cwl'

  def setUp(self):
    self.output_dir = tempfile.mkdtemp()

  def tearDown(self):
    shutil.rmtree(self.output_dir)

  def test_writes_json_order(self):
    p = PredictionRunner(self.workflow, self.sequence, self.model, self.config, self.output_dir)
    p.write_json_order()

  def test_fails_with_missing_sequence(self):
    with self.assertRaises(ValueError):
      p = PredictionRunner(self.workflow, None, self.model, self.config, self.output_dir)

  def test_fails_with_missing_model(self):
    with self.assertRaises(ValueError):
      p = PredictionRunner(self.workflow, self.sequence, None, self.config, self.output_dir)

  def test_fails_with_missing_config(self):
    with self.assertRaises(ValueError):
      p = PredictionRunner(self.workflow, self.sequence, self.model, None, self.output_dir)


