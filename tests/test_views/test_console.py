# Standard Library
import logging

# First Party Library
from src.views import console


def test_set_logger() -> None:
    logger = console.set_logger(__name__)
    assert logger.name == "test_console"
    assert isinstance(logger, logging.Logger)
