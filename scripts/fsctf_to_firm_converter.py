#!/usr/bin/env python3
"""
FSCTF to FIRM Converter

This script systematically replaces all instances of 'FSCTF' with 'FIRM' across the codebase.
It handles various formats including case sensitivity and produces a detailed report of changes.

Usage:
    python fsctf_to_firm_converter.py [--dry-run]

Options:
    --dry-run    Preview changes without actually modifying files

Author: FIRM Research Team
Created: 2024
"""

import os
import re
import argparse
from pathlib import Path
import subprocess
from typing import List, Dict, Tuple, Set

# Mapping for various forms of FSCTF
REPLACEMENTS = {
    'FSCTF': 'FIRM',
    'fsctf': 'firm',
    'Fsctf': 'Firm'
}

# Extensions to process
EXTENSIONS_TO_PROCESS = {
    '.py', '.md', '.tex', '.bib', '.txt', '.json', '.ipynb', '.yml', '.yaml', '.csv'
}

# Directories to exclude
DIRS_TO_EXCLUDE = {
    '.git', 'venv', 'env', '.vscode', '__pycache__', '.ipynb_checkpoints',
}

# Files that should be excluded (keep FSCTF references)
FILES_TO_EXCLUDE = {
    'CHANGELOG.md',
    'LICENSE',
    'legacy_notes.md',
    'history.txt',
    'fsctf_to_firm_converter.py'  # Don't modify this script itself
}


def find_files_with_fsctf(base_dir: str) -> List[str]:
    """Find all files containing 'FSCTF' in any form."""
    result = []
    try:
        # Use grep to find files containing FSCTF (faster than Python scanning)
        cmd = ['grep', '-r', '-l', 'FSCTF\\|fsctf\\|Fsctf', base_dir]
        output = subprocess.check_output(cmd, stderr=subprocess.PIPE, universal_newlines=True)
        result = output.strip().split('\n')
        # Filter out empty strings
        result = [f for f in result if f]
    except subprocess.CalledProcessError:
        # grep returns error code if no matches found
        return []
    
    # Filter for appropriate file extensions and exclude directories
    filtered_result = []
    for file_path in result:
        path = Path(file_path)
        
        # Skip files in excluded directories
        if any(excluded_dir in path.parts for excluded_dir in DIRS_TO_EXCLUDE):
            continue
            
        # Skip excluded files
        if path.name in FILES_TO_EXCLUDE:
            continue
            
        # Skip files with extensions we don't want to process
        if path.suffix not in EXTENSIONS_TO_PROCESS:
            continue
            
        filtered_result.append(file_path)
        
    return filtered_result


def replace_in_file(file_path: str, dry_run: bool = False) -> Tuple[int, Dict[str, int]]:
    """
    Replace FSCTF with FIRM in a file.
    
    Args:
        file_path: Path to the file
        dry_run: If True, don't actually modify the file
        
    Returns:
        Tuple of (total replacements, breakdown by replacement type)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    replacement_counts = {old: 0 for old in REPLACEMENTS.keys()}
    
    # Perform replacements
    for old, new in REPLACEMENTS.items():
        # Count replacements
        replacement_counts[old] = content.count(old)
        # Replace
        content = content.replace(old, new)
    
    total_replacements = sum(replacement_counts.values())
    
    # Only write if changes were made and not in dry-run mode
    if not dry_run and content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return total_replacements, replacement_counts


def main():
    """Main function to convert FSCTF to FIRM."""
    parser = argparse.ArgumentParser(description='Convert FSCTF to FIRM across the codebase')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without modifying files')
    args = parser.parse_args()
    
    # Get the project base directory (current directory)
    base_dir = os.getcwd()
    
    # Find all files containing FSCTF
    print(f"Searching for files containing FSCTF in {base_dir}...")
    files = find_files_with_fsctf(base_dir)
    
    if not files:
        print("No files found containing FSCTF.")
        return
    
    print(f"Found {len(files)} files containing FSCTF.")
    
    # Process each file
    total_files_modified = 0
    total_replacements = 0
    total_by_type = {old: 0 for old in REPLACEMENTS.keys()}
    
    for file_path in files:
        try:
            replacements, counts_by_type = replace_in_file(file_path, dry_run=args.dry_run)
            
            if replacements > 0:
                total_files_modified += 1
                total_replacements += replacements
                
                # Update counts by type
                for old, count in counts_by_type.items():
                    total_by_type[old] += count
                
                # Print details for this file
                print(f"{file_path}: {replacements} replacements")
                for old, count in counts_by_type.items():
                    if count > 0:
                        print(f"  - {old} → {REPLACEMENTS[old]}: {count}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Print summary
    print("\n" + "="*60)
    mode = "DRY RUN - No changes made" if args.dry_run else "APPLIED CHANGES"
    print(f"SUMMARY ({mode}):")
    print(f"Total files modified: {total_files_modified}")
    print(f"Total replacements: {total_replacements}")
    print("Breakdown by type:")
    for old, count in total_by_type.items():
        if count > 0:
            print(f"  - {old} → {REPLACEMENTS[old]}: {count}")
    
    if args.dry_run:
        print("\nThis was a dry run. To actually apply changes, run without --dry-run")
    

if __name__ == "__main__":
    main()
