import click
from common_options import apply_github_options
from gh.issues.get import get_issue
from github import Github
from loguru import logger


@click.command()
@apply_github_options
@click.option("--issue_number", type=int, help="Issue number to close")
def close_issue(token, owner, repo, issue_number) -> None:
    """
    Close an issue for a given repository

    Args:
        token (str): GitHub access token.
        owner (str): Repository owner.
        repo (str): Repository name.
        issue_number (int): Issue number to close.

    Returns:
        None
    """
    g = Github(token)
    repo = g.get_repo(f"{owner}/{repo}")
    issue = get_issue(issue_number)
    close_gh_issue(issue)


def close_gh_issue(issue) -> None:
    """
    Close an issue for a given repository

    Args:
        issue (github.Issue.Issue): A GitHub issue object.

    Returns:
        None
    """

    issue.edit(state="closed")
    logger.info(f"Closed issue #{issue.number}")
