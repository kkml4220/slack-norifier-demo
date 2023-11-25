# Standard Library
import logging
import logging.handlers


def set_logger(module_name: str) -> logging.Logger:
    logger = logging.getLogger(module_name)
    logger.handlers.clear()

    streamHandler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] (%(filename)s | %(funcName)s | %(lineno)s) %(message)s"
    )

    streamHandler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)

    return logger
