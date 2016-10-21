#!/bin/bash
source ../env/bin/activate
mkdir -p temp/t
cwltool --tmpdir-prefix=$(pwd)/temp/t --tmp-outdir-prefix=$(pwd)/temp/t preference-workflow.cwl preference-workflow-job.json
rm -r temp
