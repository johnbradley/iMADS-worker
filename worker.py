from predict_service.runner import PredictionRunner


class WorkerException(Exception):
    pass


class PredictionsWorker(object):

    def __init__(self, config):
        self.config = config

    @staticmethod
    def extract_predictions(result):
        return result.get('path')

    def run(self, sequence_file, model_identifier):
        workflow = PredictionRunner.predict_workflow()
        runner = PredictionRunner(workflow,
                                  sequence_file,
                                  model_identifier,
                                  self.config.config_file,
                                  self.config.model_files_dir,
                                  self.config.output_dir)
        return self.extract_predictions(runner.run())
