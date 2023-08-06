#!/usr/bin/env python3
"""
"""
import logging


def get_default_logger(name):

    logger = logging.getLogger(name)

    FORMAT = "[%(levelname)s %(lineno)s:%(name)s.%(funcName)s()] %(message)s"

    logging.basicConfig(format=FORMAT)

    logger.setLevel(logging.DEBUG)

    return logger