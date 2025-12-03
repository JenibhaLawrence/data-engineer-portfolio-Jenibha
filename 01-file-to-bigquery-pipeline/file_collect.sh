#!/bin/bash
# Collect files from multiple Unix application servers

SOURCE_DIR="/app/data/input"
LANDING_DIR="/central_server/landing"

echo "Collecting files..."
scp user@app1:$SOURCE_DIR/* $LANDING_DIR/
scp user@app2:$SOURCE_DIR/* $LANDING_DIR/

echo "File collection completed."
