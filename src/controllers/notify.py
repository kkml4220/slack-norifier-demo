# Third Party Library
import requests

# First Party Library
from src.models.client import Client
from src.schema import TemplateArgs


def slack_with_template(template_file: str, template_args: TemplateArgs) -> requests.Response:
    client = Client(template_file=template_file)
    response = client.send(template_args)
    return response
