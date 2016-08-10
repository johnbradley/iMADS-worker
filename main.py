from runner import PredictionRunner
import argparse

def arg_parser():
  parser = argparse.ArgumentParser(description='Executor for predict-tf-binding')
  parser.add_argument("--workflow", type=str, default="predict-workflow.cwl")
  parser.add_argument("--sequence-file", type=str, help="FASTA file with sequences", required=True)
  parser.add_argument("--model-identifier", type=str, help="identifier for model, e.g. E2F1_0001(JS)", required=True)
  parser.add_argument("--config-file-path", type=str, help="YAML metadata file containing configuration parameters", required=True)
  parser.add_argument("--model-files-directory", type=str, help="Location of model files referenced in config YAML", required=True)
  parser.add_argument("--output-directory", type=str, help="Location of output predictions", required=True)
  return parser

def main(workflow, sequence_file, model_identifier, config_file_path, model_files_directory, output_directory):
  PredictionRunner(workflow, sequence_file, model_identifier, config_file_path, model_files_directory, output_directory).run()

if __name__ == '__main__':
  parser = arg_parser()
  args = parser.parse_args()
  main(args.workflow, args.sequence_file, args.model_identifier, args.config_file_path, args.model_files_directory, args.output_directory)
