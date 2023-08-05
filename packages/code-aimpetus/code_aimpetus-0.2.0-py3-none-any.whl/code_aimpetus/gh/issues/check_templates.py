import click
from common_options import apply_github_token
from loguru import logger

from code_aimpetus.gh.utility import get_repo


@click.command()
@apply_github_token
def get_issue_templates(token, owner, repo):
    """
    Get issue templates in a given repository

    Args:
        token (str): GitHub access token.
        owner (str): Repository owner.
        repo (str): Repository name.

    Returns:
    """
    repo = get_repo(token, owner, repo)
    issue_templates = []

    try:
        # Check for ISSUE_TEMPLATE.md in the root directory
        issue_templates.append(repo.get_contents("ISSUE_TEMPLATE.md"))
        logger.info("Found: ISSUE_TEMPLATE.md")
    except Exception:
        pass

    try:
        # Check for issue templates in the .github/ISSUE_TEMPLATE/ directory
        issue_template_dir = repo.get_contents(".github/ISSUE_TEMPLATE")

        for content in issue_template_dir:
            if content.type == "file" and content.name.endswith(".md"):
                issue_templates.append(content)
                logger.info(f"Found: {content.path}")
    except Exception:
        pass

    if not issue_templates:
        logger.info("No issue templates found.")
    return issue_templates
