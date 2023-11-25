from typing import TypedDict, Literal


class StatusSchema(TypedDict):
    status: Literal["success", "error"]


class TemplateArgs(TypedDict):
    """テンプレートの引数"""

    title: str
    status: StatusSchema
    description: str
