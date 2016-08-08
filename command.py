import os

class PredictionCommandGenerator(object):
  def __init__(self, config, sequence_file, output_file_pattern, model_file_directory=None):
    self.config = config
    self.sequence_file = sequence_file
    self.output_file_pattern = output_file_pattern
    self.model_file_directory = model_file_directory

  def generate_commands(self):
    commands = list()
    model_filenames = list(self.config.model_filenames)
    if len(model_filenames) == len(self.config.cores):
      pass # Pair up cores and models in each command
    if len(model_filenames) == 1 and len(self.config.cores) > 1:
      # Original models were trained on multiple cores
      # Use same model file in multiple commands
      model_filenames = self.config.model_filenames * len(self.config.cores)
    for i in range(len(model_filenames)):
      model_file = model_filenames[i]
      if self.model_file_directory is not None:
        model_file = os.path.join(self.model_file_directory, model_file)
      core = self.config.cores[i]
      kmers = ','.join([str(k) for k in self.config.kmers])
      command = ['predict_tf_binding.py',
                 '-S', self.sequence_file,
                 '-m', model_file, '-c', core,
                 '-w', str(self.config.width), '-k', kmers]
      if(self.config.transform):
        command.append('-t')
      command.extend(['-o', self.output_file_pattern.format(i)])
      commands.append(command)
    return commands
