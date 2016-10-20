cwlVersion: v1.0
class: Workflow
requirements:
  - class: ScatterFeatureRequirement
inputs:
  sequence: File
  models1: File[]
  models2: File[]
  cores: string[]
  width: int
  kmers: int[]
  slope_intercept: boolean
  transform: boolean
  tf1: string
  tf2: string
  output_filename: string
outputs:
  preferences:
    type: File
    outputSource: name_output/output
steps:
  predict1:
    run: predict-tf-binding.cwl
    scatter: [model, core]
    scatterMethod: dotproduct
    in:
      sequence: sequence
      model: models1
      core: cores
      width: width
      kmers: kmers
      slope_intercept: slope_intercept
      transform: transform
    out: [predictions]
  predict2:
    run: predict-tf-binding.cwl
    scatter: [model, core]
    scatterMethod: dotproduct
    in:
      sequence: sequence
      model: models2
      core: cores
      width: width
      kmers: kmers
      slope_intercept: slope_intercept
      transform: transform
    out: [predictions]
  combine1:
    run: combine.cwl
    in:
      input_files: predict1/predictions
    out: [combined]
  combine2:
    run: combine.cwl
    in:
      input_files: predict2/predictions
    out: [combined]
  preference:
    run: predict-tf-preference.cwl
    in:
      tf1: tf1
      tf1_bed_file: combine1/combined
      tf2: tf2
      tf2_bed_file: combine2/combined
    out: [preferences]
  # filter:
  # change_precision?
  name_output:
    run: cat.cwl
    in:
      input_file: preference/preferences
      output_filename: output_filename
    out: [output]


