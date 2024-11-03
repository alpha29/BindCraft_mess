import atexit as _atexit
import os
import sys

from loguru import logger as loguru_logger

LOGURU_LOG_LEVEL = os.getenv("BINDCRAFT_LOG_LEVEL", "INFO")

# I will probably regret this.
#   https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.configure
# For future reference, here's somebody who wrapped Loguru into a logger for a Django application.
#   https://github.com/anyant/rssant/blob/master/rssant_common/logger.py
#   https://github.com/anyant/rssant/blob/master/rssant_common/loguru_patch.py
#   https://github.com/anyant/rssant/blob/master/rssant_common/django_setup.py
#   https://github.com/anyant/rssant/blob/master/rssant/wsgi.py
# That said, whatever.  I just want a well-formatted logfile, with some logging configuration (level, etc) loaded from a config file - and this is at least a start toward that.
# Friggin' A, even simple Python logging is a headache.
# ...You know what, this was probably stupid.  I think logger.add() was the right call, not logger.configure.
#   https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.add
#   https://github.com/Delgan/loguru#take-the-tour

# Because I never remember what __all__ does:
#   https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python
__all__ = ["logger"]

LOGURU_LOG_FORMAT = (
    "<level>{level: <8}| </level>"
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}| </green>"
    "<cyan>{name}:{line:<4d}| </cyan>"
    "<level>{message}</level>"
)

# Maybe gonna need another handler at some point, but this is fine for now
LOGURU_HANDLER = {
    "sink": sys.stdout,
    "level": LOGURU_LOG_LEVEL,
    "colorize": True,
    "format": LOGURU_LOG_FORMAT,
    # The internet claims diagnose and backtrace may deadlock.  Maybe?  Don't know.
    # But, official docs state that diagnose may leak info in prod, so beware
    "backtrace": True,
    "diagnose": False,
}

loguru_logger.configure(handlers=[LOGURU_HANDLER])

logger = loguru_logger
logger.add("bindcraft.log", level=LOGURU_LOG_LEVEL, rotation="1 day", compression="zip", serialize=False, format="{time} | {level} | {name}:{function}:{line} - {message}")

# ...Look, at this point I'm just guessing
# _atexit.register(logger.remove)
