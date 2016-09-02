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
  filter_threshold: float
  family: string
  tf1_x: string
  tf1_y: string
  tf2_y: string
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
      predictions1: combine1/combined
      predictions2: combine2/combined
      family: family
      tf1_x: tf1_x
      tf1_y: tf1_y
      tf2_y: tf2_y
    out: [preferences]
  change_precision:
    run: change-precision.cwl
    in:
      input_file: preference/preferences
    out: [changed]
  name_output:
    run: cat.cwl
    in:
      input_file: change_precision/changed
      output_filename: output_filename
    out: [output]


