#!/usr/bin/env bash
set -e
if [ -z "$1" ]; then
  echo "Usage: bash scripts/install_to_project.sh /path/to/project"
  exit 1
fi
python "$(dirname "$0")/init_submodule_project.py" "$1"
