#!/usr/bin/env python3
"""
Prepare a new release of codebase-ai-prompt-generator.

This script:
1. Updates the version in codebase_prompt_gen/__init__.py
2. Creates a git commit with the new version
3. Creates a git tag for the new version

Usage:
    python scripts/prepare_release.py [major|minor|patch]
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path


def get_current_version():
    """Get the current version from __init__.py."""
    init_file = Path("codebase_prompt_gen/__init__.py")
    with open(init_file, "r") as f:
        content = f.read()

    match = re.search(r'__version__ = ["\']([^"\']+)["\']', content)
    if not match:
        raise ValueError("Could not find version in __init__.py")

    return match.group(1)


def update_version(version_file, new_version):
    """Update the version in __init__.py."""
    with open(version_file, "r") as f:
        content = f.read()

    content = re.sub(
        r'__version__ = ["\']([^"\']+)["\']', f'__version__ = "{new_version}"', content
    )

    with open(version_file, "w") as f:
        f.write(content)

    print(f"Updated version to {new_version} in {version_file}")


def increment_version(version, release_type):
    """Increment the version according to the release type."""
    major, minor, patch = map(int, version.split("."))

    if release_type == "major":
        return f"{major + 1}.0.0"
    elif release_type == "minor":
        return f"{major}.{minor + 1}.0"
    elif release_type == "patch":
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError(f"Invalid release type: {release_type}")


def git_commit_and_tag(version):
    """Create a git commit and tag for the new version."""
    try:
        # Commit the version change
        subprocess.run(["git", "add", "codebase_prompt_gen/__init__.py"], check=True)
        subprocess.run(["git", "commit", "-m", f"Bump version to {version}"], check=True)

        # Create a tag
        tag = f"v{version}"
        subprocess.run(["git", "tag", "-a", tag, "-m", f"Release {tag}"], check=True)

        print(f"Created commit and tag for {version}")
        print(f"Push the changes and tag with: git push origin main && git push origin {tag}")
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Prepare a new release")
    parser.add_argument(
        "release_type", choices=["major", "minor", "patch"], help="The type of release to prepare"
    )
    args = parser.parse_args()

    # Ensure we're in the project root
    if not Path("codebase_prompt_gen/__init__.py").exists():
        print("This script must be run from the project root directory.")
        sys.exit(1)

    current_version = get_current_version()
    new_version = increment_version(current_version, args.release_type)

    print(f"Current version: {current_version}")
    print(f"New version: {new_version}")

    # Confirm with user
    response = input("Do you want to continue? [y/N] ")
    if response.lower() != "y":
        print("Aborted.")
        sys.exit(0)

    # Update version
    update_version("codebase_prompt_gen/__init__.py", new_version)

    # Commit and tag
    response = input("Do you want to create a git commit and tag? [y/N] ")
    if response.lower() == "y":
        git_commit_and_tag(new_version)

    print("Release preparation complete!")


if __name__ == "__main__":
    main()
