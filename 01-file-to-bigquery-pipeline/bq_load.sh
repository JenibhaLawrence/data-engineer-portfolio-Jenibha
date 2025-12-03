#!/bin/bash
# Load files from GCS → BigQuery table

DATASET="telecom"
TABLE="cdr_staging"

FILE_URI="gs://jenibha-data-bucket/input/*.csv"

bq load \
  --source_format=CSV \
  --autodetect \
  $DATASET.$TABLE \
  "$FILE_URI"

echo "Data loaded into BigQuery."
