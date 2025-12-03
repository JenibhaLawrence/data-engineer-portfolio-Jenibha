#!/bin/bash
# Upload files from landing server to Google Cloud Storage

LANDING_DIR="/central_server/landing"
GCS_BUCKET="gs://jenibha-data-bucket/input/"

echo "Uploading to GCS..."
gsutil cp $LANDING_DIR/* $GCS_BUCKET

echo "Upload completed."
