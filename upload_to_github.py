import os
import base64
from pathlib import Path

# Get all files
files = []
for root, dirs, filenames in os.walk('.'):
    # Skip .git and __pycache__
    if '.git' in root or '__pycache__' in root:
        continue
    for filename in filenames:
        if filename == 'upload_to_github.py':
            continue
        filepath = os.path.join(root, filename)
        relpath = os.path.relpath(filepath, '.')
        files.append(relpath)

# Print file list and base64 encoded content for GitHub upload
for filepath in sorted(files):
    try:
        with open(filepath, 'rb') as f:
            content = f.read()
            b64_content = base64.b64encode(content).decode('utf-8')
            
        print(f"=== FILE: {filepath} ===")
        print(f"Path: {filepath}")
        print(f"Base64 Length: {len(b64_content)}")
        print(f"Content (first 100 chars): {b64_content[:100]}...")
        print()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        print()
