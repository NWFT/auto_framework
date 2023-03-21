import logging
import os

import settings
file_name = os.path.join(settings.BASE_DIR, 'logs/') + 'logfile.log'

# DEBUG->INFO->WARNING->ERROR->CRITICAL


def get_logger(name, filename=file_name, debug=False, fmt=None, mode='a', encoding='utf-8'):

    # create a logger
    logger = logging.getLogger(name)

    # In default, file with warning, console with debug
    if debug:
        file_level = logging.DEBUG
        console_level = logging.DEBUG
    else:
        file_level = logging.WARNING
        console_level = logging.INFO

    # config formatter
    if fmt is None:
        fmt = '%(asctime)s %(levelname)s [%(filename)s-->lines:%(lineno)d]:%(message)s'
    file_formatter = logging.Formatter(fmt)
    console_formatter = logging.Formatter(fmt)

    # setting file handler and log level
    file_handler = logging.FileHandler(filename=filename, mode=mode, encoding=encoding)
    file_handler.setLevel(file_level)
    file_handler.setFormatter(file_formatter)
    # setting console handler(console level & formater)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(console_formatter)

    # assign settings to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    # logger will retrieve log at DEBUG level (xx->logger->file-handler->file(yy))
    logger.setLevel(logging.DEBUG)

    return logger


if __name__ == '__main__':
    logger = get_logger(__name__)
    logger.info("XXXXXX")