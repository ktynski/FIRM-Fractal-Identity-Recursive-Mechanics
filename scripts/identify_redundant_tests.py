#!/usr/bin/env python3
"""
Identify redundant test files for cleanup.

This script analyzes the testing directory to identify redundant test files
that match the patterns defined in the cleanup recommendations.
"""

import os
from pathlib import Path
from collections import defaultdict
import argparse

def find_redundant_tests(test_dir: str = "testing", patterns: list = None, show_groups: bool = False) -> dict:
    """
    Find redundant test files based on specified patterns.

    Args:
        test_dir: Directory containing test files
        patterns: List of patterns indicating redundant tests
        show_groups: Whether to group redundant tests by base name

    Returns:
        Dictionary of redundant test files
    """
    if patterns is None:
        patterns = ['_additional', '_more', '_extra', '_smoke', '_deep', '_comprehensive']

    # Will track base name -> redundant test files
    redundant_test_groups = defaultdict(list)

    # Path must exist
    test_path = Path(test_dir)
    if not test_path.exists() or not test_path.is_dir():
        print(f"Test directory not found: {test_dir}")
        return {}

    # Walk the test directory
    redundant_count = 0
    for root, _, files in os.walk(test_path):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                if any(pattern in file for pattern in patterns):
                    file_path = os.path.join(root, file)

                    # Extract base name (before pattern)
                    base_name = None
                    for pattern in patterns:
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

    # Report overall counts
    print(f"Found {redundant_count} redundant test files matching patterns: {', '.join(patterns)}")
    print(f"These are grouped into {len(redundant_test_groups)} base test types")

    # Optionally show detailed groups
    if show_groups:
        print("\nRedundant test groups:")
        for base_name, files in sorted(redundant_test_groups.items()):
            print(f"\n{base_name}: {len(files)} redundant files")
            for file in sorted(files):
                print(f"  - {file}")

    return redundant_test_groups

def suggest_cleanup_strategy(redundant_groups: dict) -> None:
    """
    Suggest a cleanup strategy for redundant test files.

    Args:
        redundant_groups: Dictionary of redundant test files grouped by base name
    """
    # Define patterns in priority order (from most to least likely to be removed)
    pattern_priority = ['_smoke', '_extra', '_additional', '_more', '_deep', '_comprehensive']

    print("\nSuggested Cleanup Strategy:")
    print("---------------------------")

    total_to_remove = 0
    total_to_keep = 0

    for base_name, files in sorted(redundant_groups.items()):
        # Keep at least one file (preferably the one without special suffixes)
        files_to_keep = []
        files_to_remove = []

        # First, check if there's a "clean" base file (without special patterns)
        base_file_pattern = base_name + ".py"
        has_base_file = any(f.endswith(base_file_pattern) for f in files)

        if has_base_file:
            # We have a clean base file, so we can potentially remove all redundant ones
            files_to_remove = files
        else:
            # No clean base file, keep the one with highest priority pattern
            remaining_files = files.copy()

            # Sort files by pattern priority (keep the last one)
            for pattern in reversed(pattern_priority):
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
            files_to_remove = [f for f in files if f not in files_to_keep]

        # Count files
        total_to_keep += len(files_to_keep)
        total_to_remove += len(files_to_remove)

        # Print suggestion for this group
        print(f"\n{base_name}: Keep {len(files_to_keep)}, Remove {len(files_to_remove)}")
        for file in sorted(files_to_keep):
            print(f"  ✅ KEEP: {file}")
        for file in sorted(files_to_remove):
            print(f"  ❌ REMOVE: {file}")

    # Print overall statistics
    print(f"\nOverall: Keep {total_to_keep} files, Remove {total_to_remove} files")
    print(f"This would reduce test count by {total_to_remove} files ({total_to_remove/(total_to_keep+total_to_remove)*100:.1f}%)")

    # Generate a cleanup command
    if total_to_remove > 0:
        print("\nCleanup Command:")
        print("---------------")
        print("To remove these files, you could use:")
        print("python scripts/cleanup_redundant_tests.py --execute")
        print("# Add --dry-run to preview without removing files")

def main():
    parser = argparse.ArgumentParser(description="Identify redundant test files")
    parser.add_argument("--test-dir", default="testing", help="Directory containing test files")
    parser.add_argument("--show-groups", action="store_true", help="Show detailed groups of redundant tests")
    args = parser.parse_args()

    redundant_groups = find_redundant_tests(args.test_dir, show_groups=args.show_groups)
    suggest_cleanup_strategy(redundant_groups)

if __name__ == "__main__":
    main()
