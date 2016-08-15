cwlVersion: v1.0
class: CommandLineTool
baseCommand: cat
inputs:
  input_file:
    type: File
    inputBinding:
      position: 1
  output_filename:
    type: string
stdout: $(inputs.output_filename)
outputs:
  output:
    type: File
    outputBinding:
      glob: $(inputs.output_filename)
