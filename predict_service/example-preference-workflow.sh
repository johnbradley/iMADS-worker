#!/bin/bash

cwltool --tmpdir-prefix=$(pwd)/temp --tmp-outdir-prefix=$(pwd)/temp preference-workflow.cwl preference-workflow-job.json
