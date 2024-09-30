#!/bin/bash

# Update AddPath script from GitHub repository
echo "==========================================="
echo "          MalwareHunterz Update Script"
echo "==========================================="
echo ""
echo "Disclaimer: Use this script at your own risk. MalwareHunterz is not responsible for any damage."
echo "==========================================="
echo ""

REPO_URL="https://github.com/yourusername/AddPath"  # Replace with your actual GitHub repository URL
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

echo "Fetching updates from $REPO_URL..."

# Clone or pull the repository
if [ -d "$SCRIPT_DIR/AddPath" ]; then
    cd "$SCRIPT_DIR/AddPath" || exit
    git pull
else
    git clone "$REPO_URL" "$SCRIPT_DIR/AddPath"
fi

# Copy the updated AddPath.py to /usr/local/bin
sudo cp "$SCRIPT_DIR/AddPath/AddPath.py" /usr/local/bin/AddPath
echo "Update complete. AddPath has been updated."
