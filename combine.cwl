cwlVersion: v1.0
class: CommandLineTool
baseCommand: cat
inputs:
  input_files:
    type: File[]
    inputBinding:
      position: 1
outputs:
  combined:
    type: stdout
