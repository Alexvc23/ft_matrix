#!/usr/bin/env python3
import os
import sys
import glob
import subprocess

def convert_py_to_ipynb(file_path):
    """Convert a single Python file to Jupyter notebook format."""
    try:
        result = subprocess.run(['py2nb', file_path], 
                             check=True, 
                             capture_output=True, 
                             text=True)
        print(f"✅ Converted: {file_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to convert {file_path}: {e.stderr}")
        return False

def main():
    if len(sys.argv) > 1:
        # Convert specific files
        files = sys.argv[1:]
    else:
        # Find all Python files in the current directory and subdirectories
        files = glob.glob("**/*.py", recursive=True)
    
    success = 0
    failed = 0
    
    for file_path in files:
        if os.path.isfile(file_path) and file_path.endswith('.py'):
            if convert_py_to_ipynb(file_path):
                success += 1
            else:
                failed += 1
    
    print(f"\nConversion complete: {success} files converted, {failed} files failed")

if __name__ == "__main__":
    main()
