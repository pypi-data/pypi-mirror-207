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
@click.option("--issue_number", type=int, help="Issue number to close")
def close_issue(token, owner, repo, issue_number):
    g = Github(token)
    repo = g.get_repo(f"{owner}/{repo}")
    issue = repo.get_issue(issue_number)
    issue.edit(state="closed")
    print(f"Closed issue #{issue_number}")
