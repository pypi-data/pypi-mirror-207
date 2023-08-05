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
def list_pull_requests(token, owner, repo):
    g = Github(token)
    repo = g.get_repo(f"{owner}/{repo}")
    pull_requests = repo.get_pulls(state="open")
    for pr in pull_requests:
        print(f"#{pr.number}: {pr.title}")
