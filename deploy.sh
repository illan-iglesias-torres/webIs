#!/usr/bin/env bash
set -euo pipefail
echo "Running custom Azure deploy script..."

# Move to repo root
REPO_DIR=$(dirname "$0")
cd "$REPO_DIR"

# Ensure python and pip available (Oryx usually handles venv)
if [ -f "antenv/bin/activate" ]; then
  source antenv/bin/activate
fi

echo "Installing requirements (if necessary)..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Done deploy script."
