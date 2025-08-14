#!/usr/bin/env python3
"""
Clean up redundant test files based on analysis.

This script builds on identify_redundant_tests.py to actually remove
redundant test files according to the suggested cleanup strategy.
"""

import os
import argparse
from pathlib import Path
from collections import defaultdict

# Patterns that indicate redundant tests (from most to least likely to be removed)
REDUNDANT_PATTERNS = ['_smoke', '_extra', '_additional', '_more', '_deep', '_comprehensive']

def find_redundant_tests(test_dir: str = "testing") -> dict:
    """
    Find redundant test files based on patterns.

    Args:
        test_dir: Directory containing test files

    Returns:
        Dictionary of redundant test files grouped by base name
    """
    # Will track base name -> redundant test files
    redundant_test_groups = defaultdict(list)

    # Path must exist
    test_path = Path(test_dir)
    if not test_path.exists() or not test_path.is_dir():
        # Test directory not found
        return {}

    # Walk the test directory
    redundant_count = 0
    for root, _, files in os.walk(test_path):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                if any(pattern in file for pattern in REDUNDANT_PATTERNS):
                    file_path = os.path.join(root, file)

                    # Extract base name (before pattern)
                    base_name = None
                    for pattern in REDUNDANT_PATTERNS:
                        if pattern in file:
                            parts = file.split(pattern)
                            if len(parts) > 1:
                                base_name = parts[0]
                                break

                    # If we can't identify a base name, use the file name
                    if base_name is None:
                        base_name = file

                    # Track group
                    redundant_test_groups[base_name].append(file_path)
                    redundant_count += 1

    # Summary: redundant test analysis completed

    return redundant_test_groups

def determine_files_to_remove(redundant_groups: dict) -> list:
    """
    Determine which files to remove based on the cleanup strategy.

    Args:
        redundant_groups: Dictionary of redundant test files grouped by base name

    Returns:
        List of files to remove
    """
    files_to_remove = []

    for base_name, files in sorted(redundant_groups.items()):
        # Keep at least one file (preferably the one without special suffixes)
        files_to_keep = []

        # First, check if there's a "clean" base file (without special patterns)
        base_file_pattern = base_name + ".py"
        has_base_file = any(f.endswith(base_file_pattern) for f in files)

        if has_base_file:
            # We have a clean base file, so we can potentially remove all redundant ones
            group_files_to_remove = files
        else:
            # No clean base file, keep the one with highest priority pattern
            remaining_files = files.copy()

            # Sort files by pattern priority (keep the last one)
            for pattern in reversed(REDUNDANT_PATTERNS):
                pattern_files = [f for f in remaining_files if pattern in f]
                if pattern_files:
                    # Keep the first one with this pattern
                    files_to_keep.append(pattern_files[0])
                    # Remove this file from consideration
                    remaining_files = [f for f in remaining_files if f != pattern_files[0]]
                    break

            # If we still haven't chosen a file to keep, keep the first one
            if not files_to_keep and remaining_files:
                files_to_keep.append(remaining_files[0])
                remaining_files.remove(files_to_keep[0])

            # All other files can be removed
            group_files_to_remove = [f for f in files if f not in files_to_keep]

        # Add to overall list
        files_to_remove.extend(group_files_to_remove)

    return files_to_remove

def cleanup_redundant_tests(test_dir: str = "testing", dry_run: bool = True, execute: bool = False) -> None:
    """
    Clean up redundant test files.

    Args:
        test_dir: Directory containing test files
        dry_run: If True, only print what would be done without removing files
        execute: If True, actually remove the files (overrides dry_run)
    """
    redundant_groups = find_redundant_tests(test_dir)
    files_to_remove = determine_files_to_remove(redundant_groups)

    # Print summary
    # Cleanup Summary
    logging.info(f"Found {len(files_to_remove)} files to remove")

    # Execute removal if requested
    if execute and not dry_run:
        print("\nRemoving files:")
        for file in sorted(files_to_remove):
            try:
                os.remove(file)
                print(f"✓ Removed: {file}")
            except Exception as e:
                print(f"✗ Error removing {file}: {e}")
    else:
        print("\nDry run mode - files that would be removed:")
        for file in sorted(files_to_remove):
            print(f"- {file}")

        if not execute:
            print("\nTo actually remove these files, run with --execute flag")

def main():
    parser = argparse.ArgumentParser(description="Clean up redundant test files")
    parser.add_argument("--test-dir", default="testing", help="Directory containing test files")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without removing files")
    parser.add_argument("--execute", action="store_true", help="Actually remove the files")
    args = parser.parse_args()

    cleanup_redundant_tests(args.test_dir, dry_run=args.dry_run, execute=args.execute)

if __name__ == "__main__":
    main()
