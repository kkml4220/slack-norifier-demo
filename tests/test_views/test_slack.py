# Standard Library
import os

# Third Party Library
from pytest import raises

# First Party Library
from src import settings
from src.views import slack


def test_get_template_dir_path() -> None:
    if settings.TEMPLATES_DIR:
        tmp_template_dir_path = os.path.join(settings.BASE_DIR, settings.TEMPLATES_DIR)
        template_dir_path = slack.get_template_dir_path()
        assert tmp_template_dir_path == template_dir_path
        assert isinstance(template_dir_path, str)
    else:
        template_dir_path = slack.get_template_dir_path()
        assert template_dir_path == os.path.join(settings.BASE_DIR, "templates")
        assert isinstance(template_dir_path, str)


def test_find_template() -> None:
    with raises(slack.NoTemplateError):
        slack.find_template("not_found_template.json")

    template_file_path = slack.find_template("test.json")
    template_dir_path = os.path.dirname(template_file_path)
    assert template_dir_path == slack.get_template_dir_path()
    assert os.path.exists(template_file_path)

    current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    template_dir_path = os.path.join(current_dir, "templates")
    test_json_file_path = os.path.join(template_dir_path, "test.json")
    assert template_file_path == test_json_file_path


def test_get_template() -> None:
    with raises(slack.NoTemplateError):
        slack.get_template("not_found_template.json")

    template_file_path = slack.find_template("test.json")
    template = slack.get_template(template_file_path)
    assert isinstance(template, str)
    content = '{\n    "name": "test"\n}'
    assert template == content
