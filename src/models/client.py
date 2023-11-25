# Standard Library
import json

# Third Party Library
import requests

# First Party Library
from src.schema import TemplateArgs
from src.settings import SLACK_WEBHOOK_URL
from src.views import console, slack

logger = console.set_logger(__name__)


class Template(object):
    def __init__(self, template_file: str):
        logger.debug({"payload": {"template_file": template_file}})
        self.template_file = template_file
        self.template = slack.get_template(self.template_file)

    def substitute(self, template_args: TemplateArgs) -> str:
        logger.debug({"payload": {"template_args": template_args}})
        if template_args["status"] == "success":
            template_args["status"] = ":white_check_mark:"
        else:
            template_args["status"] = ":x:"
        substituted_template = self.template.substitute(template_args)
        logger.debug({"template": substituted_template})
        return substituted_template


class Client(object):
    def __init__(
        self,
        url: str = SLACK_WEBHOOK_URL,
        template_file: str = "notify.txt",
    ) -> None:
        logger.debug({"payload": {"url": url, "template_file": template_file}})
        self.__headers = {"Content-Type": "application/json"}
        self.__url = url
        self.tempalte = Template(template_file)

    def send(self, template_args: TemplateArgs) -> requests.Response:
        self.template = self.tempalte.substitute(template_args)
        contents = json.loads(self.template)
        logger.info("Sending a message to Slack...")
        response = requests.post(
            self.__url,
            headers=self.__headers,
            data=json.dumps(contents),
        )
        assert response.status_code == 200
        logger.info("Successfully sent a message to Slack.")
        return response
