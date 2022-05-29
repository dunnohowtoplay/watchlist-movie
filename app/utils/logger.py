import logging
from functools import lru_cache


@lru_cache()
def get_logger():
    logger = logging.getLogger('application_log')

    return logger


logger = get_logger()