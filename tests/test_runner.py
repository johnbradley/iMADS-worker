import shutil
import tempfile
from unittest import TestCase

from runner import PredictionRunner


class PredictionRunnerTestCase(TestCase):
    sequence = 'tests/test_sequence.fa'
    model = 'ABCD_1234(AB)'
    config = 'tests/test_config.yaml'
    workflow = 'tests/test_workflow.cwl'
    models_dir = '/models'

    def setUp(self):
        self.output_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.output_dir)

    def test_writes_json_order(self):
        p = PredictionRunner(self.workflow, self.sequence, self.model, self.config, self.models_dir, self.output_dir)
        p.write_json_order()

    def test_fails_with_missing_sequence(self):
        with self.assertRaises(ValueError):
            PredictionRunner(self.workflow, None, self.model, self.config, self.models_dir, self.output_dir)

    def test_fails_with_missing_model(self):
        with self.assertRaises(ValueError):
            PredictionRunner(self.workflow, self.sequence, None, self.config, self.models_dir, self.output_dir)

    def test_fails_with_missing_config(self):
        with self.assertRaises(ValueError):
            PredictionRunner(self.workflow, self.sequence, self.model, None, self.models_dir, self.output_dir)
