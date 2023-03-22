#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" This file contains the main program """
import sys
import logging
import argparse
# TODO: Replace PACKAGE_NAME with your own
from PACKAGE_NAME.utils.logger import Logger
from PACKAGE_NAME.MAIN_CLASS_NAME import MAIN_CLASS_NAME

__author__ = "Marco Espinosa"
__email__ = "marco@marcoespinosa.es"
__date__ = "22/03/2023"
__version__ = "1.0"
__development__ = True

__application_name__ = "Template Main"


def configure_logger(verbose, console):  # pragma: no cover
    """ Method for configuring default logging options """
    log_level = logging.INFO if not verbose else logging.DEBUG
    log_file = f'{__application_name__.replace(" ", "").lower()}.log'

    return Logger.get_logger(__application_name__,
                             log_level,
                             log_file,
                             console)


def get_arguments():  # pragma: no cover
    """ Method to retrieve application arguments """
    # Configure arguments
    parser = argparse.ArgumentParser(description=__application_name__)
    parser.add_argument('-v',
                        '--verbose',
                        help="Set verbose option",
                        dest="verbose",
                        required=False,
                        action='store_true')
    parser.add_argument('-c',
                        '--console-logging',
                        help="Set console logging option",
                        dest="console",
                        required=False,
                        action='store_true')

    return parser


def exit_with_errors(logger, error):  # pragma: no cover
    """ Method to log the last error and exit the application with value 1 """
    logger.error(error)
    sys.exit(1)


def main():  # pragma: no cover
    """ Main method """

    # Get application arguments
    parser = get_arguments()
    args = parser.parse_args()

    # Get verbose argument if passsed
    verbose = bool(args.verbose)

    # Get console argument if passed
    console = bool(args.console)

    # Configure logger
    logger = configure_logger(verbose, console)

    # TODO: Check for mandatory arguments
    # if args.arg1 is None and args.args2 is None:
    #     parser.print_help()
    #     exit_with_errors(logger, "At least one argument has to be given!")

    try:
        # TODO: Initialize your instance
        prg = MAIN_CLASS_NAME(name=__application_name__)
        prg.run()

        # Global catching exceptions because we catch and raise specific exceptions
        # in each class.
    except Exception as error:
        exit_with_errors(logger, error)

    # Exit the application with success
    sys.exit(0)


if __name__ == "__main__":
    main()
