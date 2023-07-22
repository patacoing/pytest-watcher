import logging
import platform

LINUX_SYSTEM = platform.system() != "Windows" and "wsl" not in platform.release().lower()

class CustomFormatter(logging.Formatter):
    grey = "\\x1b[38;21m" if LINUX_SYSTEM else ""
    yellow = "\\x1b[33;21m" if LINUX_SYSTEM else ""
    red = "\\x1b[31;21m" if LINUX_SYSTEM else ""
    bold_red = "\\x1b[31;1m" if LINUX_SYSTEM else ""
    reset = "\\x1b[0m" if LINUX_SYSTEM else ""
    format = "%(asctime)s - [%(levelname)s] - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())

logger.addHandler(ch)
