#!/bin/bash
set -e

echo "Starting repository creation..."

# Check for gh and git
if ! command -v gh &> /dev/null; then
    echo "Error: gh CLI not found. Please install GitHub CLI."
    exit 1
fi
if ! command -v git &> /dev/null; then
    echo "Error: git not found. Please install git."
    exit 1
fi

# Check authentication
if ! gh auth status > /dev/null 2>&1; then
    echo "Error: Not authenticated with gh. Please run 'gh auth login' or set GH_TOKEN."
    exit 1
fi

# Generate repo name with timestamp
TIMESTAMP=$(date +%s)
REPO_NAME="hello-world-${TIMESTAMP}"
REPO_DESCRIPTION="A simple Hello World repository created by OpenClaw Assistant"

# Create temporary directory
WORKDIR="/home/admin/.openclaw/workspace/${REPO_NAME}"
mkdir -p "$WORKDIR"
cd "$WORKDIR"

# Initialize git repo
git init
git branch -M main

# Create README.md
cat > README.md << EOF
# ${REPO_NAME}

${REPO_DESCRIPTION}

This repository was created automatically by OpenClaw Assistant on $(date).

## Usage

\`\`\`bash
python hello.py
\`\`\`
EOF

# Create a simple Python script
cat > hello.py << EOF
#!/usr/bin/env python3
"""
A simple Hello World script.
"""
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
EOF

# Make the script executable
chmod +x hello.py

# Initial commit
git add .
git commit -m "Initial commit: Hello World repository"

# Create repository on GitHub with main as default branch and push
REPO_URL=$(gh repo create "${REPO_NAME}" --description "${REPO_DESCRIPTION}" --public --source=. --push --remote origin --default-branch main --jq .htmlUrl 2>/dev/null)
if [ -z "$REPO_URL" ]; then
    echo "Error: Failed to create repository via gh CLI."
    exit 1
fi

echo "Repository created successfully: ${REPO_URL}"
echo "Pushed to main branch."

# Output summary
SUMMARY_FILE="/home/admin/.openclaw/workspace/repo_creation_summary.txt"
cat > "$SUMMARY_FILE" << EOF
Repository: ${REPO_NAME}
URL: ${REPO_URL}
Description: ${REPO_DESCRIPTION}
Created at: $(date)
EOF

echo "Summary written to $SUMMARY_FILE"