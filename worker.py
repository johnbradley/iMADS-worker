from predict_service.runner import PredictionRunner
import json

class WorkerException(Exception):
    pass

class PredictionsWorker(object):

    @staticmethod
    def load_config(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)

    def __init__(self, config_path):
        self.config = PredictionsWorker.load_config(config_path)

    def _make_prediction_job(self, sequence_file, model_identifier):
        job = dict(self.config)
        job['input_sequence_file'] = sequence_file
        job['model_identifier'] = model_identifier
        return job

    def run(self, sequence_file, model_identifier):
        job = self._make_prediction_job(sequence_file, model_identifier)
        workflow = PredictionRunner.predict_workflow()
        runner = PredictionRunner(workflow,
                                  sequence_file,
                                  model_identifier,
                                  job['config_file_path'],
                                  job['model_files_directory'],
                                  job['output_directory'])
        return runner.run()
