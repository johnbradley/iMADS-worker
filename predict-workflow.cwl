cwlVersion: v1.0
class: Workflow
requirements:
  - class: ScatterFeatureRequirement
inputs:
  sequence: File
  models: File[]
  cores: string[]
  width: int
  kmers: int[]
  slope_intercept: boolean
  transform: boolean
  filter_threshold: float
  output_filename: string
outputs:
  predictions:
    type: File
    outputSource: name_output/output
steps:
  predict:
    run: predict-tf-binding.cwl
    scatter: [model, core]
    scatterMethod: dotproduct
    in:
      sequence: sequence
      model: models
      core: cores
      width: width
      kmers: kmers
      slope_intercept: slope_intercept
      transform: transform
    out: [predictions]
  combine:
    run: combine.cwl
    in:
      input_files: predict/predictions
    out: [combined]
  filter:
    run: filter.cwl
    in:
      input_file: combine/combined
      filter_threshold: filter_threshold
    out: [filtered]
  sort:
    run: sort.cwl
    in:
      input_file: filter/filtered
    out: [sorted]
  change_precision:
    run: change-precision.cwl
    in:
      input_file: sort/sorted
    out: [changed]
  name_output:
    run: cat.cwl
    in:
      input_file: change_precision/changed
      output_filename: output_filename
    out: [output]


