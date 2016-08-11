import datetime

import json
import os
import StringIO
from cwljob import CwlJobGenerator
from cwltool.main import main as cwl_main
from load import ConfigLoader


def timestamp(fmt='%Y-%m-%d_%H-%M-%S'):
    """
    Returns a timestamp suitable for prefixing a filename
    Parameters
    ----------
    fmt: alternate strftime format to use

    Returns
    -------
    A string containing the timestamp
    """
    return datetime.datetime.now().strftime(fmt)


class ConfigNotFoundException(Exception):
    pass

class RunnerException(Exception):
    pass

class PredictionRunner:
    """
    Class to encapsulate running of prediction on custom sequences using a CWL workflow and internal model/metadata
    """
    def __init__(self, workflow, sequence_file, model_identifier, config_file_path, model_files_directory,
                 output_directory):
        """
        Creates a PredictionRunner ready to run
        Parameters
        ----------
        workflow: Name of the CWL workflow to run
        sequence_file: FASTA-format sequence file
        model_identifier: Identifier for the model (e.g. E2F1_0001(JS)) in the config file
        config_file_path: Path to the tracks.yaml config file
        model_files_directory: Directory containing model files referenced in above config file
        output_directory: Where to store output data and intermediate JSON jobs

        """
        self.workflow = workflow
        self.sequence_file = sequence_file
        self.model_identifier = model_identifier
        self.config_file_path = config_file_path
        self.model_files_directory = model_files_directory
        self.output_directory = output_directory
        # Force config and job loading to validate inputs
        self._load()

    def _load(self):
        """
        Instantiates other child objects from passed in file parameters. Designed to fail early.

        Returns
        -------
        None

        """
        self._load_config()
        self._load_job_generator()

    def _load_config(self):
        """
        Uses a ConfigLoader to populate self.config, based on a single model identifier. Raises ConfigNotFoundException
        if model identifier not found or other error
        Returns
        -------
        None

        """
        loader = ConfigLoader(self.model_identifier, self.config_file_path)
        if loader.config is None:
            raise ConfigNotFoundException(
                'Configuration not found for model {} at path {}'.format(self.model_identifier, self.config_file_path))
        self.config = loader.config

    def _load_job_generator(self):
        """
        Sets self.job_generator to a CwlJobGenerator, based on config, sequence_file, and data dir
        Returns
        -------
        None

        """
        self.job_generator = CwlJobGenerator(self.config, self.sequence_file, self.model_files_directory)

    @property
    def order_file_name(self):
        """
        Generates a JSON file name based on the timestamp, sequence file, and model
        Returns
        -------
        String containing a file name to use for the JSON job

        """
        return '{}_{}_{}-prediction.json'.format(timestamp(), os.path.basename(self.sequence_file),
                                                 self.model_identifier)

    @property
    def order_file_path(self):
        """
        Concatenates output_directory and the order_file_name
        Returns
        -------
        Full path to the order file

        """
        return os.path.join(self.output_directory, self.order_file_name)

    def write_json_order(self):
        """
        Writes the job_generator's job order to the file at self.order_file_name
        Returns
        -------
        None
        """
        with open(self.order_file_path, 'w') as f:
            self.job_generator.write_json(f)

    def _run_workflow(self):
        """
        Runs a workflow using cwltool.main. Sets results into self.result for parsing
        Raises an exception if CWL workflow didn't run
        Returns
        -------
        CWL output 'object' in a dictionary
        """
        out, err = StringIO.StringIO(), StringIO.StringIO()
        rc = cwl_main([self.workflow, self.order_file_path], stdout=out, stderr=err)
        out_value, err_value = out.getvalue(), err.getvalue()
        out.close()
        err.close()
        if rc == 0:
            # parse the output data into a dictionary
            self.result = json.loads(out_value)
        else:
            raise RunnerException(err_value)

    def run(self):
        """
        Runs predictions, based on the initializer parameters.
        Returns
        -------
        Dictionary object, with path and checksum about predictions file

        """
        self.write_json_order()
        self._run_workflow()
        return self.result['predictions']
