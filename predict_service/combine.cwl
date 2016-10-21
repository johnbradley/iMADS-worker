cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['combine_predictions_sql.py']
requirements:
  DockerRequirement:
    dockerPull: dukegcb/predict-tf-binding
inputs:
  input_files:
    type: File[]
    inputBinding:
      position: 1
outputs:
  combined:
    type: stdout
