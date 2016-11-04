import os

BASE_URL = "BASE_URL"
OUTPUT_DIR = "OUTPUT_DIR"
MODEL_FILES_DIR = "MODEL_FILES_DIR"
PREDICTIONS_CONFIG_FILE = "PREDICTIONS_CONFIG_FILE"
PREFERENCES_CONFIG_FILE = "PREFERENCES_CONFIG_FILE"
WORKER_USERNAME = "WORKER_USERNAME"
WORKER_PASSWORD = "WORKER_PASSWORD"
TMP_PREFIX = "TMP_PREFIX"

class Config(object):

   def __init__(self):
      """
      Parameters
      ----------
      base_url: URL to the tf-dna-predictions webserver API
      output_dir: Writable directory for generated predictions
      model_files_dir: Readable directory where .model files are stored
      predictions_config_file: Path to the tracks-predictions.yaml config file providing metadata for model files
      preferences_config_file: Path to the tracks-preferences.yaml config file providing metadata for model files
      worker_username: str: username required for worker specific prediction API endpoints
      worker_password: str: password required for worker specific prediction API endpoints
      tmp_prefix: str: prefix to use for CWL tmpdir-prefix and tmp-outdir-prefix
      """

      self.base_url = os.environ.get(BASE_URL)
      self.output_dir = os.environ.get(OUTPUT_DIR)
      self.model_files_dir = os.environ.get(MODEL_FILES_DIR)
      self.predictions_config_file = os.environ.get(PREDICTIONS_CONFIG_FILE)
      self.preferences_config_file = os.environ.get(PREFERENCES_CONFIG_FILE)
      self.worker_username = os.environ.get(WORKER_USERNAME)
      self.worker_password = os.environ.get(WORKER_PASSWORD)
      self.tmp_prefix = os.environ.get(TMP_PREFIX)
