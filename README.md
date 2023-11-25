# slack-norifier-demo

[![CI](https://github.com/kkml4220/slack-norifier-demo/actions/workflows/CI.yml/badge.svg)](https://github.com/kkml4220/slack-norifier-demo/actions/workflows/CI.yml)

`Python`で`Slack`に通知を送るデモアプリケーション

## Thumbnail

![thumbnail](./images/thumbnail.png)

## Installation

```bash
pip install poetry
poetry install
```

## Usage

デモは次のコマンドで実行できます。

```bash
poetry run python main.py
# or
poetry shell
python main.py
```

また、`main.py`の関数内で`template_args`に次のような任意の辞書型オブジェクトを与えることで実際の通知内容をカスタマイズすることができます。

```json
{
  "title": "Hello, World!",
  "status": "success",
  "description": "Hello, World!"
}
```

```python
def main() -> None:
    notify.slack_with_template(
        template_file="notify.txt",
        template_args={
            "title": "Hello, World!",
            "status": "success",
            "description": "Hello, World!",
        },
    )
```
