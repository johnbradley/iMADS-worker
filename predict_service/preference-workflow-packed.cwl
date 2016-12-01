{
    "cwlVersion": "v1.0", 
    "$graph": [
        {
            "cwlVersion": "v1.0", 
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
            "name": "#cat.cwl", 
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
            "package": "file:///Users/jpb67/Documents/work/iMADS-worker/predict_service/cat.cwl", 
            "baseCommand": "cat", 
            "class": "CommandLineTool", 
            "id": "#cat.cwl"
        }, 
        {
            "cwlVersion": "v1.0", 
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
            "name": "#predict-tf-binding.cwl", 
            "package": "file:///Users/jpb67/Documents/work/iMADS-worker/predict_service/predict-tf-binding.cwl", 
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
            "cwlVersion": "v1.0", 
            "inputs": [
                {
                    "default": "preferences.bed", 
                    "inputBinding": {
                        "position": 5
                    }, 
                    "type": "string", 
                    "id": "#predict-tf-preference.cwl/output_filename"
                }, 
                {
                    "inputBinding": {
                        "position": 1
                    }, 
                    "type": "string", 
                    "id": "#predict-tf-preference.cwl/tf1"
                }, 
                {
                    "inputBinding": {
                        "position": 3
                    }, 
                    "type": "File", 
                    "id": "#predict-tf-preference.cwl/tf1_bed_file"
                }, 
                {
                    "inputBinding": {
                        "position": 2
                    }, 
                    "type": "string", 
                    "id": "#predict-tf-preference.cwl/tf2"
                }, 
                {
                    "inputBinding": {
                        "position": 4
                    }, 
                    "type": "File", 
                    "id": "#predict-tf-preference.cwl/tf2_bed_file"
                }
            ], 
            "name": "#predict-tf-preference.cwl", 
            "package": "file:///Users/jpb67/Documents/work/iMADS-worker/predict_service/predict-tf-preference.cwl", 
            "outputs": [
                {
                    "outputBinding": {
                        "glob": "$(inputs.output_filename)"
                    }, 
                    "type": "File", 
                    "id": "#predict-tf-preference.cwl/preferences"
                }
            ], 
            "baseCommand": "predict-tf-preference.R", 
            "class": "CommandLineTool", 
            "id": "#predict-tf-preference.cwl", 
            "hints": [
                {
                    "dockerPull": "dukegcb/predict-tf-preference", 
                    "class": "DockerRequirement"
                }
            ]
        }, 
        {
            "cwlVersion": "v1.0", 
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
            "name": "#combine.cwl", 
            "package": "file:///Users/jpb67/Documents/work/iMADS-worker/predict_service/combine.cwl", 
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
            "cwlVersion": "v1.0", 
            "inputs": [
                {
                    "default": "filtered-preferences.bed", 
                    "type": "string", 
                    "id": "#filter-tf-preference-threshold.cwl/output_bed_file_name"
                }, 
                {
                    "inputBinding": {
                        "position": 3
                    }, 
                    "type": "File", 
                    "id": "#filter-tf-preference-threshold.cwl/prefs_bed_file"
                }, 
                {
                    "inputBinding": {
                        "position": 1
                    }, 
                    "type": "File", 
                    "id": "#filter-tf-preference-threshold.cwl/tf1_bed_file"
                }, 
                {
                    "inputBinding": {
                        "position": 4
                    }, 
                    "type": "float", 
                    "id": "#filter-tf-preference-threshold.cwl/tf1_threshold"
                }, 
                {
                    "inputBinding": {
                        "position": 2
                    }, 
                    "type": "File", 
                    "id": "#filter-tf-preference-threshold.cwl/tf2_bed_file"
                }, 
                {
                    "inputBinding": {
                        "position": 5
                    }, 
                    "type": "float", 
                    "id": "#filter-tf-preference-threshold.cwl/tf2_threshold"
                }
            ], 
            "name": "#filter-tf-preference-threshold.cwl", 
            "stdout": "$(inputs.output_bed_file_name)", 
            "outputs": [
                {
                    "outputBinding": {
                        "glob": "$(inputs.output_bed_file_name)"
                    }, 
                    "type": "File", 
                    "id": "#filter-tf-preference-threshold.cwl/filtered_preferences"
                }
            ], 
            "package": "file:///Users/jpb67/Documents/work/iMADS-worker/predict_service/filter-tf-preference-threshold.cwl", 
            "baseCommand": [
                "filter-preference-threshold.py", 
                "--spaces"
            ], 
            "class": "CommandLineTool", 
            "id": "#filter-tf-preference-threshold.cwl", 
            "hints": [
                {
                    "dockerPull": "dukegcb/predict-tf-preference", 
                    "class": "DockerRequirement"
                }
            ]
        }, 
        {
            "cwlVersion": "v1.0", 
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
                    "id": "#main/models1"
                }, 
                {
                    "type": {
                        "items": "File", 
                        "type": "array"
                    }, 
                    "id": "#main/models2"
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
                    "type": "string", 
                    "id": "#main/tf1"
                }, 
                {
                    "type": "float", 
                    "id": "#main/tf1_threshold"
                }, 
                {
                    "type": "string", 
                    "id": "#main/tf2"
                }, 
                {
                    "type": "float", 
                    "id": "#main/tf2_threshold"
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
            "name": "#main", 
            "outputs": [
                {
                    "outputSource": "#main/name_output/output", 
                    "type": "File", 
                    "id": "#main/preferences"
                }
            ], 
            "id": "#main", 
            "steps": [
                {
                    "out": [
                        "#main/combine1/combined"
                    ], 
                    "run": "#combine.cwl", 
                    "id": "#main/combine1", 
                    "in": [
                        {
                            "source": "#main/predict1/predictions", 
                            "id": "#main/combine1/input_files"
                        }
                    ]
                }, 
                {
                    "out": [
                        "#main/combine2/combined"
                    ], 
                    "run": "#combine.cwl", 
                    "id": "#main/combine2", 
                    "in": [
                        {
                            "source": "#main/predict2/predictions", 
                            "id": "#main/combine2/input_files"
                        }
                    ]
                }, 
                {
                    "out": [
                        "#main/filter/filtered_preferences"
                    ], 
                    "run": "#filter-tf-preference-threshold.cwl", 
                    "id": "#main/filter", 
                    "in": [
                        {
                            "source": "#main/preference/preferences", 
                            "id": "#main/filter/prefs_bed_file"
                        }, 
                        {
                            "source": "#main/combine1/combined", 
                            "id": "#main/filter/tf1_bed_file"
                        }, 
                        {
                            "source": "#main/tf1_threshold", 
                            "id": "#main/filter/tf1_threshold"
                        }, 
                        {
                            "source": "#main/combine2/combined", 
                            "id": "#main/filter/tf2_bed_file"
                        }, 
                        {
                            "source": "#main/tf2_threshold", 
                            "id": "#main/filter/tf2_threshold"
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
                            "source": "#main/filter/filtered_preferences", 
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
                        "#main/predict1/model", 
                        "#main/predict1/core"
                    ], 
                    "in": [
                        {
                            "source": "#main/cores", 
                            "id": "#main/predict1/core"
                        }, 
                        {
                            "source": "#main/core_start", 
                            "id": "#main/predict1/core_start"
                        }, 
                        {
                            "source": "#main/kmers", 
                            "id": "#main/predict1/kmers"
                        }, 
                        {
                            "source": "#main/models1", 
                            "id": "#main/predict1/model"
                        }, 
                        {
                            "source": "#main/sequence", 
                            "id": "#main/predict1/sequence"
                        }, 
                        {
                            "source": "#main/slope_intercept", 
                            "id": "#main/predict1/slope_intercept"
                        }, 
                        {
                            "source": "#main/transform", 
                            "id": "#main/predict1/transform"
                        }, 
                        {
                            "source": "#main/width", 
                            "id": "#main/predict1/width"
                        }
                    ], 
                    "scatterMethod": "dotproduct", 
                    "id": "#main/predict1", 
                    "out": [
                        "#main/predict1/predictions"
                    ]
                }, 
                {
                    "run": "#predict-tf-binding.cwl", 
                    "scatter": [
                        "#main/predict2/model", 
                        "#main/predict2/core"
                    ], 
                    "in": [
                        {
                            "source": "#main/cores", 
                            "id": "#main/predict2/core"
                        }, 
                        {
                            "source": "#main/core_start", 
                            "id": "#main/predict2/core_start"
                        }, 
                        {
                            "source": "#main/kmers", 
                            "id": "#main/predict2/kmers"
                        }, 
                        {
                            "source": "#main/models2", 
                            "id": "#main/predict2/model"
                        }, 
                        {
                            "source": "#main/sequence", 
                            "id": "#main/predict2/sequence"
                        }, 
                        {
                            "source": "#main/slope_intercept", 
                            "id": "#main/predict2/slope_intercept"
                        }, 
                        {
                            "source": "#main/transform", 
                            "id": "#main/predict2/transform"
                        }, 
                        {
                            "source": "#main/width", 
                            "id": "#main/predict2/width"
                        }
                    ], 
                    "scatterMethod": "dotproduct", 
                    "id": "#main/predict2", 
                    "out": [
                        "#main/predict2/predictions"
                    ]
                }, 
                {
                    "out": [
                        "#main/preference/preferences"
                    ], 
                    "run": "#predict-tf-preference.cwl", 
                    "id": "#main/preference", 
                    "in": [
                        {
                            "source": "#main/tf1", 
                            "id": "#main/preference/tf1"
                        }, 
                        {
                            "source": "#main/combine1/combined", 
                            "id": "#main/preference/tf1_bed_file"
                        }, 
                        {
                            "source": "#main/tf2", 
                            "id": "#main/preference/tf2"
                        }, 
                        {
                            "source": "#main/combine2/combined", 
                            "id": "#main/preference/tf2_bed_file"
                        }
                    ]
                }
            ], 
            "class": "Workflow"
        }
    ]
}