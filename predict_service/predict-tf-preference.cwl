cwlVersion: v1.0
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: dukegcb/predict-tf-preference
inputs:
  tf1:
    type: string
    inputBinding:
      position: 1
  tf2:
    type: string
    inputBinding:
      position: 2
  tf1_bed_file:
    type: File
    inputBinding:
      position: 3
  tf2_bed_file:
    type: File
    inputBinding:
      position: 4
  output_filename:
    type: string
    default: "preferences.bed"
    inputBinding:
      position: 5
outputs:
  preferences:
    type: File
    outputBinding:
      glob: $(inputs.output_filename)

baseCommand: predict-tf-preference.R
