from src import settings
import os


def test_base_dir() -> None:
    assert settings.BASE_DIR
    assert settings.BASE_DIR == os.path.dirname(os.path.dirname(__file__))


def test_templates() -> None:
    assert settings.TEMPLATES_DIR
    assert settings.TEMPLATES_DIR == "templates"
