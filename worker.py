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
        if '_vs_' in model_identifier:
            strategy = PredictionRunner.strategy_preference
            config_file = self.config.preferences_config_file
        else:
            strategy = PredictionRunner.strategy_predict
            config_file = self.config.predictions_config_file
        runner = PredictionRunner(sequence_file,
                                  model_identifier,
                                  config_file,
                                  self.config.model_files_dir,
                                  self.config.output_dir,
                                  strategy,
                                  self.config.tmp_prefix)
        return self.extract_predictions(runner.run())
