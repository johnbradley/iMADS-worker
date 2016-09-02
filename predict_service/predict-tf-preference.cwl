cwlVersion: v1.0
class: CommandLineTool
baseCommand: predict-tf-preference.R
requirements:
  DockerRequirement:
    dockerPull: predict-tf-preference
#Usage: predict-tf-preference.R tf1.bed tf2.bed output.bed family tf1_x tf1_y tf2_y
inputs:
  predictions1:
    type: File
    inputBinding:
      position: 1
  predictions2:
    type: File
    inputBinding:
      position: 2
  output_filename:
    type: string
    default: "preferences.bed"
    inputBinding:
      position: 3
  family:
    type: string
    inputBinding:
      position: 4
  tf1_x:
    type: string
    inputBinding:
      position: 5
  tf1_y:
    type: string
    inputBinding:
      position: 6
  tf2_y:
    type: string
    inputBinding:
      position: 7
outputs:
  preferences:
    type: File
    outputBinding:
      glob: $(inputs.output_filename)
