import click
from common_options import apply_github_options
from github.Issue import Issue
from github.PaginatedList import PaginatedList
from github.Repository import Repository
from loguru import logger

from code_aimpetus.gh.utility import get_repo


@click.command()
@apply_github_options
def list_issues(token: str, owner: str, repo: str) -> PaginatedList[Issue]:
    """
    List all issues for a given repository

    Args:
        token (str): GitHub access token.
        owner (str): Repository owner.
        repo (str): Repository name.

    Returns:
        github.PaginatedList.PaginatedList[github.Issue.Issue]:
            A list of GitHub issue objects.
    """
    repo: Repository = get_repo(token, owner, repo)
    issues = repo.get_issues(state="open")
    for issue in issues:
        logger.info(f"#{issue.number}: {issue.title}")
    return issues
