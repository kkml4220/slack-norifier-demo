# Standard Library
import os

# First Party Library
from src.settings import BASE_DIR


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
            template_dir_path = os.path.join(BASE_DIR, settings.TEMPLATES_DIR)
    except ImportError:
        pass

    if not template_dir_path:
        template_dir_path = os.path.join(BASE_DIR, "templates")

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
        raise NoTemplateError(f"Could not find {template_file}")
    return template_file_path


def get_template(template_file: str):
    """テンプレートファイルを返します

    Args:
        template_file (str): テンプレートファイルのパス

    Returns:
        str: テンプレートファイルの中身
    """
    template_file_path = find_template(template_file)
    with open(template_file_path, "r", encoding="utf-8") as template:
        contents = template.read()
        return contents
