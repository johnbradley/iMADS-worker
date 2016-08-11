cwlVersion: v1.0
baseCommand: filter.py
requirements:
  DockerRequirement:
    dockerPull: dukegcb/predict-tf-binding
class: CommandLineTool
inputs:
  input_file:
    type: File
    inputBinding:
      position: 1
  filter_threshold:
    type: float
    inputBinding:
      position: 2
  delimiter:
    type: string
    default: ' '
    inputBinding:
      position: 3
outputs:
  filtered:
    type: stdout

