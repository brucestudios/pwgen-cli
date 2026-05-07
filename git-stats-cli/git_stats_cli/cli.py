import click
import json
import csv
from datetime import datetime, timedelta
from .core import GitStatsAnalyzer
from .utils import format_output, parse_date

@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Git Stats CLI - Analyze Git repository statistics."""
    pass

@cli.command()
@click.option('--since', default=None, help='Start date for analysis (e.g., "2026-01-01" or "6 months ago")')
@click.option('--until', default=None, help='End date for analysis (e.g., "2026-05-01")')
@click.option('--author', default=None, help='Filter by author (email or name)')
@click.option('--ignore-merges', is_flag=True, help='Ignore merge commits')
def summary(since, until, author, ignore_merges):
    """Show summary statistics for the repository."""
    analyzer = GitStatsAnalyzer()
    stats = analyzer.get_summary(since=since, until=until, author=author, ignore_merges=ignore_merges)
    click.echo(format_output(stats, format='text'))

@cli.command()
@click.option('--since', default=None, help='Start date for analysis')
@click.option('--until', default=None, help='End date for analysis')
@click.option('--top', default=10, help='Number of top contributors to show')
@click.option('--format', 'output_format', type=click.Choice(['text', 'json', 'csv', 'markdown']), default='text', help='Output format')
def contributors(since, until, top, output_format):
    """Show contributor statistics."""
    analyzer = GitStatsAnalyzer()
    contributors = analyzer.get_contributors(since=since, until=until, top=top)
    click.echo(format_output(contributors, format=output_format))

@cli.command()
@click.option('--since', default=None, help='Start date for analysis')
@click.option('--until', default=None, help='End date for analysis')
@click.option('--interval', type=click.Choice(['day', 'week', 'month']), default='week', help='Time interval for grouping')
@click.option('--format', 'output_format', type=click.Choice(['text', 'json', 'csv', 'markdown']), default='text', help='Output format')
def timeline(since, until, interval, output_format):
    """Show commit timeline."""
    analyzer = GitStatsAnalyzer()
    timeline_data = analyzer.get_timeline(since=since, until=until, interval=interval)
    click.echo(format_output(timeline_data, format=output_format))

@cli.command()
@click.option('--since', default=None, help='Start date for analysis')
@click.option('--until', default=None, help='End date for analysis')
@click.option('--file-types', default='', help='Comma-separated list of file extensions to include (e.g., ".py,.js")')
@click.option('--format', 'output_format', type=click.Choice(['text', 'json', 'csv', 'markdown']), default='text', help='Output format')
def churn(since, until, file_types, output_format):
    """Show file change statistics (code churn)."""
    analyzer = GitStatsAnalyzer()
    file_types_list = [ft.strip() for ft in file_types.split(',') if ft.strip()] if file_types else None
    churn_data = analyzer.get_churn(since=since, until=until, file_types=file_types_list)
    click.echo(format_output(churn_data, format=output_format))

@cli.command()
@click.option('--since', default=None, help='Start date for analysis')
@click.option('--until', default=None, help='End date for analysis')
@click.option('--format', 'output_format', type=click.Choice(['text', 'json', 'csv', 'markdown']), default='markdown', help='Output format')
@click.option('--output', default=None, help='Output file path (if not provided, prints to stdout)')
def report(since, until, output_format, output):
    """Generate a comprehensive report."""
    analyzer = GitStatsAnalyzer()
    report_data = analyzer.generate_report(since=since, until=until)
    formatted = format_output(report_data, format=output_format)
    if output:
        with open(output, 'w') as f:
            f.write(formatted)
        click.echo(f"Report written to {output}")
    else:
        click.echo(formatted)

if __name__ == '__main__':
    cli()