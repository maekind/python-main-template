#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" This file contains a class template """

import logging
from PACKAGE_NAME.utils.logger import Logger
from PACKAGE_NAME.utils.decorators import Logging

__author__ = "Marco Espinosa"
__email__ = "marco@marcoespinosa.es"
__date__ = "22/03/2023"
__version__ = "1.0"
__development__ = True

# TDOO: Replace MAIN_CLASS_NAME with your own


class MAIN_CLASS_NAME:
    """ This class is a template for your main package """

    def __init__(self, name: str) -> None:
        """ Default constructor """
        # Initialize logger (also needed for decorators!)
        self._name = name

        # Configure logger
        self._logger = logging.getLogger(self._name)

        # TODO: Your initialization goes here:

    @Logging.trace_info("Launching run method ...")
    def run(self):
        """ Method to execute your class staff """

    def __repr__(self) -> str:
        """ Return the class printed version """
        return f"{self.__class__.__name__}"
