import os

import click
from github import Github


@click.command()
@click.option(
    "--token",
    help="Your GitHub access token",
    default=os.environ.get("GITHUB_TOKEN", ""),
)
@click.option(
    "--owner", help="Repository owner", default=os.environ.get("GITHUB_OWNER", "")
)
@click.option(
    "--repo", help="Repository name", default=os.environ.get("GITHUB_REPO", "")
)
def list_issues(token, owner, repo):
    g = Github(token)
    repo = g.get_repo(f"{owner}/{repo}")
    issues = repo.get_issues(state="open")
    for issue in issues:
        print(f"#{issue.number}: {issue.title}")
    return issues
