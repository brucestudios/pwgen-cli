"""Core functionality for changelog generation."""

import subprocess
import re
from datetime import datetime
from typing import List, Dict, Optional


def get_git_log(
    since: Optional[str] = None,
    until: Optional[str] = None,
    format_str: str = "%H %s %b%d",
) -> List[str]:
    """Get git log entries as a list of strings.

    Args:
        since: Start date (e.g., "2026-01-01") or relative (e.g., "2.weeks.ago").
        until: End date (e.g., "2026-05-01") or relative.
        format_str: Git log format string.

    Returns:
        List of formatted log lines.
    """
    cmd = ["git", "log"]
    if since:
        cmd.extend(["--since", since])
    if until:
        cmd.extend(["--until", until])
    cmd.extend(["--pretty=format:" + format_str])

    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return output.strip().split("\n") if output.strip() else []
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Git command failed: {e.output}") from e


def parse_commit_line(line: str) -> Dict[str, str]:
    """Parse a formatted git log line into components.

    Expected format: "%H %s %b%d" (hash, subject, body with trailers).

    Args:
        line: A single line from git log.

    Returns:
        Dictionary with keys: hash, subject, body.
    """
    parts = line.split(" ", 2)
    if len(parts) < 3:
        return {"hash": parts[0] if parts else "", "subject": "", "body": ""}
    hash_val, subject, body = parts
    return {"hash": hash_val, "subject": subject, "body": body}


def generate_changelog(
    since: Optional[str] = None,
    until: Optional[str] = None,
    pattern: Optional[str] = None,
) -> str:
    """Generate a changelog from git commits.

    Args:
        since: Start date for commits (e.g., "2026-01-01").
        until: End date for commits (e.g., "2026-05-01").
        pattern: Optional regex pattern to filter commit subjects.

    Returns:
        Formatted changelog as a string.
    """
    lines = get_git_log(since=since, until=until)
    commits = [parse_commit_line(line) for line in lines if line]

    if pattern:
        regex = re.compile(pattern, re.IGNORECASE)
        commits = [c for c in commits if regex.search(c["subject"])]

    # Group by conventional commit types (feat, fix, etc.) if present
    sections: Dict[str, List[Dict]] = {}
    for commit in commits:
        subject = commit["subject"]
        # Check for conventional commit pattern: type(scope): description
        match = re.match(r"^(\w+)(?:\([^)]+\))?:\s+(.+)", subject)
        if match:
            commit_type = match.group(1).lower()
            description = match.group(2)
        else:
            commit_type = "other"
            description = subject

        sections.setdefault(commit_type, []).append(
            {"hash": commit["hash"], "description": description, "body": commit["body"]}
        )

    # Order of sections (common conventional commit types)
    ordered_types = [
        "feat",
        "fix",
        "docs",
        "style",
        "refactor",
        "test",
        "chore",
        "perf",
        "ci",
        "build",
        "other",
    ]
    # Filter to only those that exist
    ordered_types = [t for t in ordered_types if t in sections]

    # Generate changelog
    now = datetime.utcnow().strftime("%Y-%m-%d")
    changelog_lines = [f"# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n## [{now}] - Unreleased\n"]

    for commit_type in ordered_types:
        # Map to human-readable section titles
        type_titles = {
            "feat": "Features",
            "fix": "Bug Fixes",
            "docs": "Documentation",
            "style": "Styles",
            "refactor": "Code Refactoring",
            "test": "Tests",
            "chore": "Chores",
            "perf": "Performance Improvements",
            "ci": "Continuous Integration",
            "build": "Build System",
            "other": "Other Changes",
        }
        title = type_titles.get(commit_type, commit_type.capitalize())
        changelog_lines.append(f"### {title}\n")
        for commit in sections[commit_type]:
            changelog_lines.append(f"- {commit['description']} ([{commit['hash'][:7]}](https://github.com/{get_remote_url()}/commit/{commit['hash']}))")
        changelog_lines.append("")  # Empty line between sections

    return "\n".join(changelog_lines)


def get_remote_url() -> str:
    """Get the remote origin URL in the format 'owner/repo'.

    Returns:
        String in the format 'owner/repo' or 'unknown/unknown' if not available.
    """
    try:
        output = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], stderr=subprocess.STDOUT, text=True
        ).strip()
        # Handle HTTPS and SSH URLs
        if output.startswith("https://github.com/"):
            return output[len("https://github.com/"):].replace(".git", "")
        elif output.startswith("git@github.com:"):
            return output[len("git@github.com:"):].replace(".git", "")
        else:
            return "unknown/unknown"
    except subprocess.CalledProcessError:
        return "unknown/unknown"


if __name__ == "__main__":
    # When run as a script, generate changelog for all time and print
    print(generate_changelog())