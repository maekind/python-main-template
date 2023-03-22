#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Logger wrapper """

import logging

__author__ = "Marco Espinosa"
__email__ = "marco@marcoespinosa.es"
__date__ = "22/03/2023"
__version__ = "1.0"
__development__ = True


class Logger:
    """ Wrapper for logging
    following a specific format """

    @staticmethod
    def get_logger(name: str, level: int, filename: str = None, console: bool = False) -> logging.Logger:
        """ Return a logger instance """
        # Create line format
        log_formatter = logging.Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
            datefmt='%d-%m-%Y %H:%M:%S')

        logger = logging.getLogger(name)
        # If console is set, configure logging to stdout
        if console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(log_formatter)
            logger.addHandler(console_handler)

        # If filename is passed, configure the file handler
        if filename:
            file_handler = logging.FileHandler(filename)
            file_handler.setFormatter(log_formatter)
            logger.addHandler(file_handler)

        # Configure level
        logger.setLevel(level)

        return logger

    def __str__(self) -> str:
        """ Return the instance printed version"""
        return f"Logger version {__version__} (c) {__author__} ({__email__})"

    def __rpr__(self) -> str:
        """ Return the class printed version """
        return f"{self.__class__.__name__}"
