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
    echo "Error: Not authenticated with gh. Please run 'gh auth login'."
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

# Create repository on GitHub (empty)
echo "Creating repository on GitHub..."
REPO_JSON=$(gh repo create "${REPO_NAME}" --description "${REPO_DESCRIPTION}" --public --confirm 2>&1)
# Extract the repo URL from output (it's printed after creation)
REPO_URL=$(echo "$REPO_JSON" | grep -o 'https://github.com/[^ ]*' | head -1)
if [ -z "$REPO_URL" ]; then
    # Try alternative: use gh api to get repo info
    REPO_INFO=$(gh api repos/brucestudios/"${REPO_NAME}" --jq '.html_url' 2>/dev/null)
    if [ -n "$REPO_INFO" ]; then
        REPO_URL="$REPO_INFO"
    else
        echo "Error: Failed to create repository or get its URL."
        echo "Output: $REPO_JSON"
        exit 1
    fi
fi

echo "Repository created: $REPO_URL"

# Add remote and push
git remote add origin "$(echo "$REPO_URL".git)"
git push -u origin main

# Set default branch to main via API (in case it was set to master)
echo "Setting default branch to main..."
gh api -X PATCH repos/brucestudios/"${REPO_NAME}" -f default_branch=main > /dev/null

echo "Repository setup complete."

# Output summary
SUMMARY_FILE="/home/admin/.openclaw/workspace/repo_creation_summary.txt"
cat > "$SUMMARY_FILE" << EOF
Repository: ${REPO_NAME}
URL: ${REPO_URL}
Description: ${REPO_DESCRIPTION}
Created at: $(date)
Default branch: main
EOF

echo "Summary written to $SUMMARY_FILE"
cat "$SUMMARY_FILE"