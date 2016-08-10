import yaml

class ConfigLoader:
  model_id_key = 'track_name'
  # Given a model identifier such as E2F4_0002(JS) and a YAML document with metadata
  def __init__(self, model_id, metadata_file_name):
    if model_id is None:
      raise ValueError('model_id is required')
    if metadata_file_name is None:
      raise ValueError('metadata_file_name is required')
    self.model_id = model_id
    self.metadata_file_name = metadata_file_name
    self._config = None

  def find_config(self):
    with open(self.metadata_file_name, 'r') as metadata_file:
      configs = yaml.load(metadata_file)
      matching_configs = [c for c in configs if c[ConfigLoader.model_id_key]  == self.model_id]
      if matching_configs:
        return matching_configs[0]
    return None

  @property
  def config(self):
    if self._config is None:
      self._config = self.find_config()
    return self._config
