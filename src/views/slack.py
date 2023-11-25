# Standard Library
import os
import string

# First Party Library
from src.settings import BASE_DIR
from src.views.console import set_logger

logger = set_logger(__name__)


def get_template_dir_path() -> str:
    """テンプレートディレクトリのパスを取得

    Returns:
        str: テンプレートディレクトリのパス
    """
    template_dir_path = None
    try:
        # First Party Library
        from src import settings

        if settings.TEMPLATES_DIR:
            logger.debug({"TEMPLATES_DIR": settings.TEMPLATES_DIR})
            template_dir_path = os.path.join(BASE_DIR, settings.TEMPLATES_DIR)
    except ImportError:
        logger.debug({"TEMPLATES_DIR": "None"})

    if not template_dir_path:
        template_dir_path = os.path.join(BASE_DIR, "templates")

    logger.debug({"template_dir_path": template_dir_path})
    return template_dir_path


class NoTemplateError(Exception):
    """テンプレートが存在しないエラー"""

    pass


def find_template(template_file: str) -> str:
    """テンプレートファイルのパスを作成

    Args:
        template_file (str): テンプレートファイルのファイル名

    Returns:
        str: テンプレートファイルのパス

    Raises:
        NoTemplateError: template_fileが存在しない場合のエラー
    """
    template_dir_path = get_template_dir_path()
    template_file_path = os.path.join(template_dir_path, template_file)

    if not os.path.exists(template_file_path):
        logger.error({"template_file_path": template_file_path})
        raise NoTemplateError(f"Could not find {template_file}")
    logger.debug({"template_file_path": template_file_path})
    return template_file_path


def get_template(template_file: str) -> string.Template:
    """テンプレートファイルを返します

    Args:
        template_file (str): テンプレートファイルのパス

    Returns:
        string.Template: テンプレートファイルの中身
    """
    logger.debug({"payload": {"template_file": template_file}})
    template_file_path = find_template(template_file)
    logger.debug({"action": "open", "template_file_path": template_file_path})
    with open(template_file_path, "r", encoding="utf-8") as template:
        contents = template.read()
        logger.debug({"action": "close", "template_file_path": template_file_path})
        return string.Template(contents)
