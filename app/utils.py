"""
Small utilities
"""
import sys
import logging

from constants import LOG_FORMATTER


def logger(file_name):
    '''

    :param file_name: File name using logger function
    :return: Logger handle
    '''
    # Create a custom logger
    logger = logging.getLogger(file_name)

    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    c_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    c_format = logging.Formatter(LOG_FORMATTER)
    c_handler.setFormatter(c_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)
    return logger