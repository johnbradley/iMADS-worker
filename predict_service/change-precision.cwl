cwlVersion: v1.0
baseCommand: ['change_precision.py','--spaces']
requirements:
  DockerRequirement:
    dockerPull: dukegcb/predict-tf-binding
class: CommandLineTool
inputs:
  input_file:
    type: File
    inputBinding:
      position: 1
  precision:
    type: int
    default: 4
    inputBinding:
      position: 2
outputs:
  changed:
    type: stdout

