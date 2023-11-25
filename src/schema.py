# Standard Library
from typing import Literal, TypedDict


class TemplateArgs(TypedDict):
    """テンプレートの引数"""

    title: str
    status: Literal["success", "error", ":white_check_mark:", ":x:"]
    description: str
