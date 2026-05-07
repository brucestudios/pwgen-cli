#!/bin/bash
set -x
REPO_NAME="test-gh-$(date +%s)"
REPO_DESCRIPTION="Test"
mkdir -p /tmp/$REPO_NAME
cd /tmp/$REPO_NAME
git init
echo "# test" > README.md
git add .
git commit -m "init"
gh repo create $REPO_NAME --description "$REPO_DESCRIPTION" --public --source=. --push --remote origin --default-branch main 2>&1