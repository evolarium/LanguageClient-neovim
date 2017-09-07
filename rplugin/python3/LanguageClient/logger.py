import logging
import tempfile

logger = logging.getLogger("LanguageClient")
with tempfile.NamedTemporaryFile(
        prefix="LanguageClient-",
        suffix=".log", delete=False) as tmp:
    tmpname = tmp.name
fileHandler = logging.FileHandler(filename=tmpname)
fileHandler.setFormatter(
    logging.Formatter(
        "%(asctime)s %(levelname)-7s [%(threadName)-10s] %(message)s",
        "%H:%M:%S"))
logger.addHandler(fileHandler)
logger.setLevel(logging.WARN)


def setLoggingLevel(level) -> None:
    """
    Set logging level.
    """
    logger.setLevel({
        "ERROR": 40,
        "WARNING": 30,
        "INFO": 20,
        "DEBUG": 10,
    }[level])
