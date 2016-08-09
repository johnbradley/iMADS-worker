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
outputs:
  predictions:
    type: File
    outputSource: combine/output
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
      filter_threshold: filter_threshold
    out: [predictions]
  combine:
    run: combine.cwl
    in:
      input_files: predict/predictions
    out: [output]
