# Standard Library
import os

from load_dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATES_DIR = "templates"


load_dotenv()

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")
