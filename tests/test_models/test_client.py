# Standard Library
from typing import Any

# Third Party Library
import pytest

# First Party Library
from src.models.client import Client, Template


class TestTemplate(object):
    def setup_method(self, method: Any) -> None:
        print("method={}".format(method.__name__))
        self.t = Template("test.txt")

    def teardown_method(self, method: Any) -> None:
        print("method={}".format(method.__name__))
        del self.t

    def test__init__(self) -> None:
        assert self.t.template_file == "test.txt"
        assert self.t.template.template == '{"name": "${name}"}'

    def test_substitute(self) -> None:
        with pytest.raises(KeyError):
            assert self.t.substitute({"foo": "bar"})  # type: ignore
        tempplate_args = {"name": "test", "status": "success"}
        assert self.t.substitute(tempplate_args) == '{"name": "test"}'  # type: ignore


class TestClient(object):
    def setup_method(self, method: Any) -> None:
        print(type(method))
        print("method={}".format(method.__name__))
        self.url = ""
        self.template_file = "test.txt"

    def teardown_method(self, method: Any) -> None:
        print("method={}".format(method.__name__))

    def test__init__(self) -> None:
        c = Client(url=self.url, template_file=self.template_file)
        assert c.tempalte.template_file == "test.txt"
        assert c.tempalte.template.template == '{"name": "${name}"}'
