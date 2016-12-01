{
    "cwlVersion": "v1.0", 
    "$graph": [
        {
            "inputs": [
                {
                    "inputBinding": {
                        "position": 1
                    }, 
                    "type": "File", 
                    "id": "#cat.cwl/input_file"
                }, 
                {
                    "type": "string", 
                    "id": "#cat.cwl/output_filename"
                }
            ], 
            "stdout": "$(inputs.output_filename)", 
            "outputs": [
                {
                    "outputBinding": {
                        "glob": "$(inputs.output_filename)"
                    }, 
                    "type": "File", 
                    "id": "#cat.cwl/output"
                }
            ], 
            "baseCommand": "cat", 
            "class": "CommandLineTool", 
            "id": "#cat.cwl"
        }, 
        {
            "inputs": [
                {
                    "inputBinding": {
                        "position": 1
                    }, 
                    "type": "File", 
                    "id": "#change-precision.cwl/input_file"
                }, 
                {
                    "default": 4, 
                    "inputBinding": {
                        "position": 2
                    }, 
                    "type": "int", 
                    "id": "#change-precision.cwl/precision"
                }
            ], 
            "outputs": [
                {
                    "type": "stdout", 
                    "id": "#change-precision.cwl/changed"
                }
            ], 
            "baseCommand": [
                "change_precision.py", 
                "--spaces"
            ], 
            "class": "CommandLineTool", 
            "id": "#change-precision.cwl", 
            "hints": [
                {
                    "dockerPull": "dukegcb/predict-tf-binding", 
                    "class": "DockerRequirement"
                }
            ]
        }, 
        {
            "inputs": [
                {
                    "inputBinding": {
                        "position": 1
                    }, 
                    "type": {
                        "items": "File", 
                        "type": "array"
                    }, 
                    "id": "#combine.cwl/input_files"
                }
            ], 
            "outputs": [
                {
                    "type": "stdout", 
                    "id": "#combine.cwl/combined"
                }
            ], 
            "baseCommand": [
                "combine_predictions_sql.py"
            ], 
            "class": "CommandLineTool", 
            "id": "#combine.cwl", 
            "hints": [
                {
                    "dockerPull": "dukegcb/predict-tf-binding", 
                    "class": "DockerRequirement"
                }
            ]
        }, 
        {
            "inputs": [
                {
                    "inputBinding": {
                        "position": 2
                    }, 
                    "type": "float", 
                    "id": "#filter.cwl/filter_threshold"
                }, 
                {
                    "inputBinding": {
                        "position": 1
                    }, 
                    "type": "File", 
                    "id": "#filter.cwl/input_file"
                }
            ], 
            "outputs": [
                {
                    "type": "stdout", 
                    "id": "#filter.cwl/filtered"
                }
            ], 
            "baseCommand": [
                "filter.py", 
                "--spaces"
            ], 
            "class": "CommandLineTool", 
            "id": "#filter.cwl", 
            "hints": [
                {
                    "dockerPull": "dukegcb/predict-tf-binding", 
                    "class": "DockerRequirement"
                }
            ]
        }, 
        {
            "inputs": [
                {
                    "inputBinding": {
                        "prefix": "--chroms", 
                        "itemSeparator": " ", 
                        "separate": true
                    }, 
                    "type": [
                        "null", 
                        {
                            "items": "string", 
                            "type": "array"
                        }
                    ], 
                    "id": "#predict-tf-binding.cwl/chroms"
                }, 
                {
                    "inputBinding": {
                        "prefix": "-c"
                    }, 
                    "type": "string", 
                    "id": "#predict-tf-binding.cwl/core"
                }, 
                {
                    "inputBinding": {
                        "prefix": "--core-start"
                    }, 
                    "type": [
                        "null", 
                        "int"
                    ], 
                    "id": "#predict-tf-binding.cwl/core_start"
                }, 
                {
                    "inputBinding": {
                        "prefix": "-k"
                    }, 
                    "type": {
                        "items": "int", 
                        "type": "array"
                    }, 
                    "id": "#predict-tf-binding.cwl/kmers"
                }, 
                {
                    "inputBinding": {
                        "prefix": "-m"
                    }, 
                    "type": "File", 
                    "id": "#predict-tf-binding.cwl/model"
                }, 
                {
                    "default": "predictions.bed", 
                    "inputBinding": {
                        "prefix": "-o"
                    }, 
                    "type": "string", 
                    "id": "#predict-tf-binding.cwl/output_filename"
                }, 
                {
                    "inputBinding": {
                        "prefix": "-s"
                    }, 
                    "type": "File", 
                    "id": "#predict-tf-binding.cwl/sequence"
                }, 
                {
                    "default": true, 
                    "inputBinding": {
                        "prefix": "--skip-size-check"
                    }, 
                    "type": "boolean", 
                    "id": "#predict-tf-binding.cwl/skip_size_check"
                }, 
                {
                    "default": false, 
                    "inputBinding": {
                        "prefix": "-i"
                    }, 
                    "type": "boolean", 
                    "id": "#predict-tf-binding.cwl/slope_intercept"
                }, 
                {
                    "default": false, 
                    "inputBinding": {
                        "prefix": "-t"
                    }, 
                    "type": "boolean", 
                    "id": "#predict-tf-binding.cwl/transform"
                }, 
                {
                    "inputBinding": {
                        "prefix": "-w"
                    }, 
                    "type": "int", 
                    "id": "#predict-tf-binding.cwl/width"
                }
            ], 
            "outputs": [
                {
                    "outputBinding": {
                        "glob": "$(inputs.output_filename)"
                    }, 
                    "type": "File", 
                    "id": "#predict-tf-binding.cwl/predictions"
                }
            ], 
            "baseCommand": "predict_tf_binding.py", 
            "class": "CommandLineTool", 
            "id": "#predict-tf-binding.cwl", 
            "hints": [
                {
                    "dockerPull": "dukegcb/predict-tf-binding", 
                    "class": "DockerRequirement"
                }
            ]
        }, 
        {
            "inputs": [
                {
                    "type": [
                        "null", 
                        "int"
                    ], 
                    "id": "#main/core_start"
                }, 
                {
                    "type": {
                        "items": "string", 
                        "type": "array"
                    }, 
                    "id": "#main/cores"
                }, 
                {
                    "type": "float", 
                    "id": "#main/filter_threshold"
                }, 
                {
                    "type": {
                        "items": "int", 
                        "type": "array"
                    }, 
                    "id": "#main/kmers"
                }, 
                {
                    "type": {
                        "items": "File", 
                        "type": "array"
                    }, 
                    "id": "#main/models"
                }, 
                {
                    "type": "string", 
                    "id": "#main/output_filename"
                }, 
                {
                    "type": "File", 
                    "id": "#main/sequence"
                }, 
                {
                    "type": "boolean", 
                    "id": "#main/slope_intercept"
                }, 
                {
                    "type": "boolean", 
                    "id": "#main/transform"
                }, 
                {
                    "type": "int", 
                    "id": "#main/width"
                }
            ], 
            "requirements": [
                {
                    "class": "ScatterFeatureRequirement"
                }
            ], 
            "outputs": [
                {
                    "outputSource": "#main/name_output/output", 
                    "type": "File", 
                    "id": "#main/predictions"
                }
            ], 
            "id": "#main", 
            "steps": [
                {
                    "out": [
                        "#main/change_precision/changed"
                    ], 
                    "run": "#change-precision.cwl", 
                    "id": "#main/change_precision", 
                    "in": [
                        {
                            "source": "#main/filter/filtered", 
                            "id": "#main/change_precision/input_file"
                        }
                    ]
                }, 
                {
                    "out": [
                        "#main/combine/combined"
                    ], 
                    "run": "#combine.cwl", 
                    "id": "#main/combine", 
                    "in": [
                        {
                            "source": "#main/predict/predictions", 
                            "id": "#main/combine/input_files"
                        }
                    ]
                }, 
                {
                    "out": [
                        "#main/filter/filtered"
                    ], 
                    "run": "#filter.cwl", 
                    "id": "#main/filter", 
                    "in": [
                        {
                            "source": "#main/filter_threshold", 
                            "id": "#main/filter/filter_threshold"
                        }, 
                        {
                            "source": "#main/combine/combined", 
                            "id": "#main/filter/input_file"
                        }
                    ]
                }, 
                {
                    "out": [
                        "#main/name_output/output"
                    ], 
                    "run": "#cat.cwl", 
                    "id": "#main/name_output", 
                    "in": [
                        {
                            "source": "#main/change_precision/changed", 
                            "id": "#main/name_output/input_file"
                        }, 
                        {
                            "source": "#main/output_filename", 
                            "id": "#main/name_output/output_filename"
                        }
                    ]
                }, 
                {
                    "run": "#predict-tf-binding.cwl", 
                    "scatter": [
                        "#main/predict/model", 
                        "#main/predict/core"
                    ], 
                    "in": [
                        {
                            "source": "#main/cores", 
                            "id": "#main/predict/core"
                        }, 
                        {
                            "source": "#main/core_start", 
                            "id": "#main/predict/core_start"
                        }, 
                        {
                            "source": "#main/kmers", 
                            "id": "#main/predict/kmers"
                        }, 
                        {
                            "source": "#main/models", 
                            "id": "#main/predict/model"
                        }, 
                        {
                            "source": "#main/sequence", 
                            "id": "#main/predict/sequence"
                        }, 
                        {
                            "source": "#main/slope_intercept", 
                            "id": "#main/predict/slope_intercept"
                        }, 
                        {
                            "source": "#main/transform", 
                            "id": "#main/predict/transform"
                        }, 
                        {
                            "source": "#main/width", 
                            "id": "#main/predict/width"
                        }
                    ], 
                    "scatterMethod": "dotproduct", 
                    "id": "#main/predict", 
                    "out": [
                        "#main/predict/predictions"
                    ]
                }
            ], 
            "class": "Workflow"
        }
    ]
}