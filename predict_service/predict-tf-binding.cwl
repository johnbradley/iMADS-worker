cwlVersion: v1.0
class: CommandLineTool
baseCommand: predict_tf_binding.py
requirements:
  DockerRequirement:
    dockerPull: dukegcb/predict-tf-binding
inputs:
  sequence:
    type: File
    inputBinding:
      prefix: -s
  chroms:
    type: string[]?
    inputBinding:
      prefix: --chroms
      itemSeparator: " "
      separate: true
  model:
    type: File
    inputBinding:
      prefix: -m
  core:
    type: string
    inputBinding:
      prefix: -c
  width:
    type: int
    inputBinding:
      prefix: -w
  kmers:
    type: int[]
    inputBinding:
      prefix: -k
  slope_intercept:
    type: boolean
    default: false
    inputBinding:
      prefix: -i
  transform:
    type: boolean
    default: false
    inputBinding:
      prefix: -t
  output_filename:
    type: string
    default: "predictions.bed"
    inputBinding:
      prefix: -o
outputs:
  predictions:
    type: File
    outputBinding:
      glob: $(inputs.output_filename)
