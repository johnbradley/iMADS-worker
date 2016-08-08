class PredictionConfig(object):

  def parse(self, initial_data):
    for key in initial_data:
      setattr(self, key, initial_data[key])

  def __init__(self, config):
    self.author_identifier = None
    self.cores = None
    self.filter_threshold = None
    self.model_filenames = None
    self.protein = None
    self.serial_number = None
    self.slope_intercept = None
    self.width = None
    self.transform = None
    self.parse(config)

