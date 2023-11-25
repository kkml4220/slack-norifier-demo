from src.controllers import notify


def main():
    notify.slack_with_template(
        template_file="notify.txt",
        template_args={
            "title": "Hello, World!",
            "status": "success",
            "description": "Hello, World!",
        },
    )


if __name__ == "__main__":
    main()
