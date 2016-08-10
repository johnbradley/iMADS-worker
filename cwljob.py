import json

def make_file_dict(path):
  return {'class': 'File', 'path': path}

class CwlJobGenerator:
  def __init__(self, config_dict, sequence_file):
    if sequence_file is None:
      raise ValueError('Sequence file is required')
    if config_dict is None:
      raise ValueError('config_dict is required')
    self.config_dict = config_dict
    self.sequence_file = sequence_file
    self._job = None

  @property
  def job(self):
    if self._job is None:
      job = dict.copy(self.config_dict)
      # If single model and multiple cores, expand models
      model_filenames = list(job['model_filenames'])
      num_models, num_cores = len(model_filenames), len(job['cores'])
      if num_cores > num_models:
        model_filenames = model_filenames * num_cores
      job['models'] = [make_file_dict(model) for model in model_filenames]
      job['sequence'] = make_file_dict(self.sequence_file)
      self._job = job
    return self._job

  def write_json(self, output_file):
    json.dump(self.job, output_file)
