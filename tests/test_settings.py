from src import settings
import os


def test_base_dir():
    assert settings.BASE_DIR
    assert settings.BASE_DIR == os.path.dirname(os.path.dirname(__file__))


def test_templates():
    assert settings.TEMPLATES_DIR
    assert settings.TEMPLATES_DIR == "templates"
