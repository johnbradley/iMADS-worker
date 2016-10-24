#!/bin/bash
source ../env/bin/activate
mkdir -p temp/t
cwltool --tmpdir-prefix=$(pwd)/temp/t --tmp-outdir-prefix=$(pwd)/temp/t predict-workflow.cwl predict-workflow-job.json
rm -r temp
