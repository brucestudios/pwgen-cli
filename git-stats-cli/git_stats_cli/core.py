import git
from datetime import datetime, timedelta
from collections import defaultdict
from typing import List, Dict, Any, Optional
import os


class GitStatsAnalyzer:
    def __init__(self, repo_path: str = None):
        if repo_path is None:
            repo_path = os.getcwd()
        self.repo = git.Repo(repo_path)

    def _parse_date(self, date_str: Optional[str]) -> Optional[datetime]:
        if date_str is None:
            return None
        # Handle relative dates like "6 months ago", "2 weeks ago", etc.
        # For simplicity, we'll only handle absolute dates in ISO format and a few relative ones.
        # In a real implementation, you might use dateparser or similar.
        try:
            return datetime.fromisoformat(date_str)
        except ValueError:
            pass

        # Handle simple relative dates
        now = datetime.now()
        if date_str.endswith(" ago"):
            value_str = date_str[:-4].strip()
            if value_str.endswith(" month"):
                try:
                    value = int(value_str.split()[0])
                    return now - timedelta(days=30 * value)
                except ValueError:
                    pass
            elif value_str.endswith(" month"):
                try:
                    value = int(value_str.split()[0])
                    return now - timedelta(days=30 * value)
                except ValueError:
                    pass
            elif value_str.endswith(" week"):
                try:
                    value = int(value_str.split()[0])
                    return now - timedelta(weeks=value)
                except ValueError:
                    pass
            elif value_str.endswith(" day"):
                try:
                    value = int(value_str.split()[0])
                    return now - timedelta(days=value)
                except ValueError:
                    pass
            elif value_str.endswith(" year"):
                try:
                    value = int(value_str.split()[0])
                    return now - timedelta(days=365 * value)
                except ValueError:
                    pass
        # If we can't parse, return None (no filter)
        return None

    def _filter_commits(self, since: Optional[datetime] = None, until: Optional[datetime] = None,
                        author: Optional[str] = None, ignore_merges: bool = False):
        commits = []
        for commit in self.repo.iter_commits():
            # Date filtering
            commit_date = datetime.fromtimestamp(commit.committed_date)
            if since and commit_date < since:
                continue
            if until and commit_date > until:
                continue
            # Author filtering
            if author:
                if author.lower() not in commit.author.email.lower() and \
                   author.lower() not in commit.author.name.lower():
                    continue
            # Ignore merge commits
            if ignore_merges and len(commit.parents) > 1:
                continue
            commits.append(commit)
        return commits

    def get_summary(self, since: Optional[str] = None, until: Optional[str] = None,
                    author: Optional[str] = None, ignore_merges: bool = False) -> Dict[str, Any]:
        since_dt = self._parse_date(since)
        until_dt = self._parse_date(until)
        commits = self._filter_commits(since=since_dt, until=until_dt, author=author, ignore_merges=ignore_merges)

        total_commits = len(commits)
        authors = set()
        total_insertions = 0
        total_deletions = 0
        for commit in commits:
            authors.add(commit.author.email)
            # We can get the stats from commit.stats if available, but note that iterating over all commits
            # and getting stats for each might be slow for large repos. We'll do it for now.
            # Alternatively, we can use the diff index.
            # For simplicity, we'll skip the detailed stats in the summary and just show commit count and authors.
            # We'll add more details if needed.

        return {
            "total_commits": total_commits,
            "total_authors": len(authors),
            "date_range": {
                "since": since_dt.isoformat() if since_dt else None,
                "until": until_dt.isoformat() if until_dt else None
            },
            "ignore_merges": ignore_merges,
            "author_filter": author
        }

    def get_contributors(self, since: Optional[str] = None, until: Optional[str] = None,
                         top: int = 10) -> List[Dict[str, Any]]:
        since_dt = self._parse_date(since)
        until_dt = self._parse_date(until)
        commits = self._filter_commits(since=since_dt, until=until_dt)

        # Count commits by author
        author_stats = defaultdict(lambda: {"commits": 0, "insertions": 0, "deletions": 0, "files_changed": 0})
        for commit in commits:
            email = commit.author.email
            name = commit.author.name
            key = (email, name)
            author_stats[key]["commits"] += 1
            # Get the stats for this commit
            stats = commit.stats.total
            author_stats[key]["insertions"] += stats.get("insertions", 0)
            author_stats[key]["deletions"] += stats.get("deletions", 0)
            author_stats[key]["files_changed"] += stats.get("files", 0)

        # Convert to list and sort by commits
        contributors = []
        for (email, name), stats in author_stats.items():
            contributors.append({
                "author": name,
                "email": email,
                "commits": stats["commits"],
                "insertions": stats["insertions"],
                "deletions": stats["deletions"],
                "files_changed": stats["files_changed"]
            })

        contributors.sort(key=lambda x: x["commits"], reverse=True)
        return contributors[:top]

    def get_timeline(self, since: Optional[str] = None, until: Optional[str] = None,
                     interval: str = 'week') -> List[Dict[str, Any]]:
        since_dt = self._parse_date(since)
        until_dt = self._parse_date(until)
        commits = self._filter_commits(since=since_dt, until=until_dt)

        # Group by interval
        if interval == 'day':
            fmt = "%Y-%m-%d"
            delta = timedelta(days=1)
        elif interval == 'week':
            fmt = "%Y-%W"  # Year-Weeknumber
            delta = timedelta(weeks=1)
        elif interval == 'month':
            fmt = "%Y-%m"
            delta = timedelta(days=30)  # Approximation
        else:
            fmt = "%Y-%m-%d"
            delta = timedelta(days=1)

        timeline = defaultdict(int)
        for commit in commits:
            commit_date = datetime.fromtimestamp(commit.committed_date)
            key = commit_date.strftime(fmt)
            timeline[key] += 1

        # Convert to list of dicts and sort by date
        result = [{"period": k, "commits": v} for k, v in timeline.items()]
        result.sort(key=lambda x: x["period"])
        return result

    def get_churn(self, since: Optional[str] = None, until: Optional[str] = None,
                  file_types: Optional[List[str]] = None) -> Dict[str, Any]:
        since_dt = self._parse_date(since)
        until_dt = self._parse_date(until)
        commits = self._filter_commits(since=since_dt, until=until_dt)

        # We'll collect stats per file
        file_stats = defaultdict(lambda: {"insertions": 0, "deletions": 0, "changes": 0})
        for commit in commits:
            # We can iterate over the files in the commit and get the stats for each file
            # However, note that getting the stats for each file in each commit can be expensive.
            # We'll do it for now for simplicity.
            try:
                # Get the commit's diff
                diff = commit.diff(commit.parents[0] if commit.parents else None, create_patch=False)
                for d in diff:
                    # d is a Diff object
                    file_path = d.b_path if d.b_path else d.a_path
                    if file_path is None:
                        continue
                    # Filter by file types if provided
                    if file_types:
                        if not any(file_path.endswith(ext) for ext in file_types):
                            continue
                    # We don't have the line-by-line stats in the diff object without parsing the patch.
                    # For simplicity, we'll skip the detailed churn per file and just count the number of changes.
                    # In a real implementation, we would use commit.stats.files or parse the patch.
                    # We'll approximate by counting the number of files changed and using the total stats for the commit.
                    # But note: we want per-file stats.
                    # Let's change approach: use commit.stats.files which gives us per-file stats.
                    pass
            except Exception:
                # If we can't get the diff, skip this commit for file-level stats
                continue

        # Instead, let's use the commit.stats.files which is available in GitPython
        # We'll reset and do it again.
        file_stats = defaultdict(lambda: {"insertions": 0, "deletions": 0, "changes": 0})
        for commit in commits:
            try:
                for file_path, stats in commit.stats.files.items():
                    if file_types:
                        if not any(file_path.endswith(ext) for ext in file_types):
                            continue
                    file_stats[file_path]["insertions"] += stats.get("insertions", 0)
                    file_stats[file_path]["deletions"] += stats.get("deletions", 0)
                    file_stats[file_path]["changes"] += stats.get("insertions", 0) + stats.get("deletions", 0)
            except Exception:
                # If we can't get the stats for this commit, skip
                continue

        # Convert to list and sort by changes (total lines changed)
        churn_list = []
        for file_path, stats in file_stats.items():
            churn_list.append({
                "file": file_path,
                "insertions": stats["insertions"],
                "deletions": stats["deletions"],
                "changes": stats["changes"]
            })

        churn_list.sort(key=lambda x: x["changes"], reverse=True)
        return {
            "files": churn_list,
            "total_files": len(churn_list)
        }

    def generate_report(self, since: Optional[str] = None, until: Optional[str] = None) -> Dict[str, Any]:
        summary = self.get_summary(since=since, until=until)
        contributors = self.get_contributors(since=since, until=until, top=10)
        timeline = self.get_timeline(since=since, until=until, interval='week')
        churn = self.get_churn(since=since, until=until)

        return {
            "summary": summary,
            "top_contributors": contributors,
            "commit_timeline": timeline,
            "code_churn": churn,
            "generated_at": datetime.now().isoformat()
        }