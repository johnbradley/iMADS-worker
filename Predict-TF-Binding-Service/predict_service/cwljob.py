import json

import os


def make_file_dict(path):
    """
    Creates a CWL "file object" - a dictionary containing two entries: class and path
    Parameters
    ----------
    path: A file path to encapsulate

    Returns
    -------
    A dictionary referencing a file, suitable for a CWL job

    """
    return {'class': 'File', 'path': path}


class CwlJobGenerator:
    """
    Generates CWL job orders - dictionaries ready for supplying to cwltool in JSON
    """
    def __init__(self, config_dict, sequence_file, model_files_directory, output_filename=None):
        """

        Parameters
        ----------
        config_dict: A dictionary containing model/track config (models, cores, slope_intercept, etc)
        sequence_file: Path to a fasta-formatted sequence file
        model_files_directory: Base directory containing model files referenced in config_dict
        output_filename: The name of the file in which to store predictions, or None to let workflow decide
        """
        if sequence_file is None:
            raise ValueError('Sequence file is required')
        if config_dict is None:
            raise ValueError('config_dict is required')
        if model_files_directory is None:
            raise ValueError('model_files_directory is required')
        self.config_dict = config_dict
        self.sequence_file = sequence_file
        self.model_files_directory = model_files_directory
        self.output_filename = output_filename
        self._job = None

    @property
    def job(self):
        """

        Returns
        -------
        A dictionary containing the parameters needed to run a CWL job based on the constructor variables
        """
        if self._job is None:
            job = dict.copy(self.config_dict)
            # If single model and multiple cores, expand models
            model_filenames = list(job['model_filenames'])
            num_models, num_cores = len(model_filenames), len(job['cores'])
            if num_cores > num_models:
                model_filenames = model_filenames * num_cores
            job['models'] = [make_file_dict(os.path.join(self.model_files_directory, model)) for model in
                             model_filenames]
            job['sequence'] = make_file_dict(self.sequence_file)
            if self.output_filename:
              job['output_filename'] = self.output_filename
            self._job = job
        return self._job

    def write_json(self, output_file):
        """
        Writes this object's job dictionary to JSON format, using the provided file object.
        Parameters
        ----------
        output_file: a file object, opened for writing

        Returns
        -------
        None

        """
        json.dump(self.job, output_file)
