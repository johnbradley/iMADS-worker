import os

BASE_URL = "BASE_URL"
OUTPUT_DIR = "OUTPUT_DIR"
MODEL_FILES_DIR = "MODEL_FILES_DIR"
CONFIG_FILE = "CONFIG_FILE"


class Config(object):

   def __init__(self):
      """
      Parameters
      ----------
      base_url: URL to the tf-dna-predictions webserver API
      output_dir: Writable directory for generated predictions
      model_files_dir: Readable directory where .model files are stored
      config_file: Path to the tracks.yaml config file providing metadata for model files
      """

      self.base_url = os.environ.get(BASE_URL)
      self.output_dir = os.environ.get(OUTPUT_DIR)
      self.model_files_dir = os.environ.get(MODEL_FILES_DIR)
      self.config_file = os.environ.get(CONFIG_FILE)
