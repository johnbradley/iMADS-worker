#!/usr/bin/env python

import argparse
import os

from runner import PredictionRunner


def arg_parser():
    """
    Creates an argument parser for command-line usage
    Returns
    -------
    Argument parser to run predictions from command-line

    """
    my_dir = os.path.dirname(os.path.realpath(__file__))
    parser = argparse.ArgumentParser(description='Executor for predict-tf-binding')
    parser.add_argument("--workflow", type=str, default=os.path.join(my_dir, "predict-workflow.cwl"))
    parser.add_argument("--sequence-file", type=str, help="FASTA file with sequences", required=True)
    parser.add_argument("--model-identifier", type=str, help="identifier for model, e.g. E2F1_0001(JS)", required=True)
    parser.add_argument("--config-file-path", type=str, help="YAML metadata file containing configuration parameters",
                        required=True)
    parser.add_argument("--model-files-directory", type=str, help="Location of model files referenced in config YAML",
                        required=True)
    parser.add_argument("--output-directory", type=str, help="Location of output predictions", required=True)
    return parser


def run(workflow, sequence_file, model_identifier, config_file_path, model_files_directory, output_directory):
    """
    Instantiates and runs a PredictionRunner

    Parameters
    ----------
    workflow: Name of the CWL workflow to run
    sequence_file: FASTA-format sequence file
    model_identifier: Identifier for the model (e.g. E2F1_0001(JS)) in the config file
    config_file_path: Path to the tracks.yaml config file
    model_files_directory: Directory containing model files referenced in above config file
    output_directory: Where to store output data and intermediate JSON jobs

    Returns
    -------
    None

    """
    predictions = PredictionRunner(workflow, sequence_file, model_identifier, config_file_path, model_files_directory,
                     output_directory).run()
    print predictions['path']

def main():
    parser = arg_parser()
    args = parser.parse_args()
    run(args.workflow, args.sequence_file, args.model_identifier, args.config_file_path, args.model_files_directory,
         args.output_directory)

if __name__ == '__main__':
    main()
