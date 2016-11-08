cwlVersion: v1.0
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: dukegcb/predict-tf-preference
inputs:
  tf1_bed_file:
    type: File
    inputBinding:
      position: 1
  tf2_bed_file:
    type: File
    inputBinding:
      position: 2
  prefs_bed_file:
    type: File
    inputBinding:
      position: 3
  tf1_threshold:
    type: float
    inputBinding:
      position: 4
  tf2_threshold:
    type: float
    inputBinding:
      position: 5
  output_bed_file_name:
    type: string
    default: "filtered-preferences.bed"
outputs:
  filtered_preferences:
    type: File
    outputBinding:
      glob: $(inputs.output_bed_file_name)

stdout:  $(inputs.output_bed_file_name)

baseCommand: ['filter-preference-threshold.py','--spaces']
