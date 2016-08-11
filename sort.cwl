cwlVersion: v1.0
class: CommandLineTool
baseCommand: ['sort', '-k1,1', '-k2,2n']
requirements:
  EnvVarRequirement:
    envDef:
      LC_COLLATE: C
inputs:
  input_file:
    type: File
    inputBinding:
      position: 1
outputs:
  sorted:
    type: stdout
