# Standard Library
import json

# Third Party Library
import requests

# First Party Library
from src.schema import TemplateArgs
from src.settings import SLACK_WEBHOOK_URL
from src.views import slack


class Template(object):
    def __init__(self, template_file: str):
        self.template = slack.get_template(template_file)

    def substitute(self, template_args: TemplateArgs) -> str:
        if template_args["status"] == "success":
            template_args["status"] = ":white_check_mark:"
        else:
            template_args["status"] = ":x:"
        return self.template.substitute(template_args)


class Client(object):
    def __init__(
        self,
        url: str = SLACK_WEBHOOK_URL,
        template_file: str = "notify.txt",
    ) -> None:
        self.__headers = {"Content-Type": "application/json"}
        self.__url = url
        self.tempalte = Template(template_file)

    def send(self, template_args: TemplateArgs) -> requests.Response:
        self.template = self.tempalte.substitute(template_args)
        contents = json.loads(self.template)
        return requests.post(
            self.__url,
            headers=self.__headers,
            data=json.dumps(contents),
        )
