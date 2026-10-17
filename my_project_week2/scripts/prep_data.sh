#!/usr/bin/env bash
set -euo pipefail
echo "[INFO] Preparing data directory structure..."
mkdir -p data
RAW_FILE="data/iris.csv"
curl -L -o $RAW_FILE https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
echo "[INFO] Downloaded sample dataset: $RAW_FILE"
echo "custom,0.1,0.2,0.3,setosa" >> $RAW_FILE
echo "[INFO] Added one synthetic row."
LINES=$(wc -l < $RAW_FILE)
echo "[REPORT] Dataset now has $LINES rows."
echo "[INFO] Done!"
