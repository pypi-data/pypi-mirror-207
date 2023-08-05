import os

from dotenv import load_dotenv

load_dotenv()

GITHUB_OWNER = os.environ.get("GITHUB_OWNER", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO = os.environ.get("GITHUB_REPO", "")

BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://:codeai@redis:6379/0")
