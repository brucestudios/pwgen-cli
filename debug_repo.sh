#!/bin/bash
set -x
set -e

REPO_NAME="test-debug-$(date +%s)"
REPO_DESCRIPTION="Test repo"

mkdir -p /tmp/${REPO_NAME}
cd /tmp/${REPO_NAME}
git init
echo "# Test" > README.md
git add .
git commit -m "initial"

# Try to create repo with gh
echo "Attempting to create repo with gh..."
OUTPUT=$(gh repo create ${REPO_NAME} --description "${REPO_DESCRIPTION}" --public --source=. --push 2>&1)
echo "OUTPUT: $OUTPUT"
echo "Exit code: $?"