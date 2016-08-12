cwlVersion: v1.0
baseCommand: ['filter.py','--spaces']
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
outputs:
  filtered:
    type: stdout

