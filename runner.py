import datetime

import os
from cwljob import CwlJobGenerator
from cwltool.main import main as cwl_main
from load import ConfigLoader


def timestamp(fmt='%Y-%m-%d_%H-%M-%S'):
    return datetime.datetime.now().strftime(fmt)


class ConfigNotFoundException(Exception):
    pass


class PredictionRunner:
    def __init__(self, workflow, sequence_file, model_identifier, config_file_path, model_files_directory,
                 output_directory):
        self.workflow = workflow
        self.sequence_file = sequence_file
        self.model_identifier = model_identifier
        self.config_file_path = config_file_path
        self.model_files_directory = model_files_directory
        self.output_directory = output_directory
        # Force config and job loading to validate inputs
        self._load()

    def _load(self):
        self._load_config()
        self._load_job_generator()

    def _load_config(self):
        loader = ConfigLoader(self.model_identifier, self.config_file_path)
        if loader.config is None:
            raise ConfigNotFoundException(
                'Configuration not found for model {} at path {}'.format(self.model_identifier, self.config_file_path))
        self.config = loader.config

    def _load_job_generator(self):
        self.job_generator = CwlJobGenerator(self.config, self.sequence_file, self.model_files_directory)

    @property
    def order_file_name(self):
        return '{}_{}_{}-prediction.json'.format(timestamp(), os.path.basename(self.sequence_file),
                                                 self.model_identifier)

    @property
    def order_file_path(self):
        return os.path.join(self.output_directory, self.order_file_name)

    def write_json_order(self):
        with open(self.order_file_path, 'w') as f:
            self.job_generator.write_json(f)

    def run(self):
        # write the order
        # Run the workflow
        self.write_json_order()
        cwl_main([self.workflow, self.order_file_path])
