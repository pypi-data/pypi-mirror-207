import click
from common_options import apply_github_options
from gh.utility import get_repo
from github.Issue import Issue
from github.Repository import Repository


@click.command()
@apply_github_options
@click.option("--issue_number", type=int, help="Issue number to close")
def get_issue(token: str, owner: str, repo: str, issue_number: int) -> Issue:
    """
    Get an issue for a given repository

    Args:
        token (str): GitHub access token.
        owner (str): Repository owner.
        repo (str): Repository name.
        issue_number (int): Issue number to get.

        Returns:
    """
    repo: Repository = get_repo(token, owner, repo)
    return repo.get_issue(issue_number)
