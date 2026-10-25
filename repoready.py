#!/usr/bin/env python3
"""Check a repository for common open-source project files."""

import argparse
from pathlib import Path

CHECKS = [
("README.md", "Add a project overview and usage instructions."),
("LICENSE", "Add a license explaining how others may use your code."),
("CONTRIBUTING.md", "Explain how people can contribute."),
("CODE_OF_CONDUCT.md", "Define expectations for community behavior."),
("tests", "Add automated tests for important functionality."),
]

def inspect_repository(root):
"""Return the status of expected files in a repository."""
results = []

for name, suggestion in CHECKS:
    path = root / name
    exists = path.is_dir() if name == "tests" else path.is_file()
    results.append((name, exists, suggestion))

return results

def main():
parser = argparse.ArgumentParser(
description="Check common open-source project files."
)
parser.add_argument(
"path",
nargs="?",
default=".",
help="Repository directory to inspect.",
)
args = parser.parse_args()

root = Path(args.path).expanduser().resolve()

if not root.is_dir():
    parser.error(f"Not a directory: {root}")

print(f"RepoReady report: {root}")
present = 0
missing = 0

for name, exists, suggestion in inspect_repository(root):
    if exists:
        print(f"[OK] {name}")
        present += 1
    else:
        print(f"[MISSING] {name} - {suggestion}")
        missing += 1

print(f"Summary: {present} present, {missing} missing.")

if name == "main":
main()