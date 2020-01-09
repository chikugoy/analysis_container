#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import pathlib
import os
import errno
import sys
import logging
import logging.config
import inspect
from pathlib import Path
from threading import Lock

sys.path.append('./')
from .singleton import Singleton


class Logger(Singleton):

    LOG_DIR_NAME = 'log'
    LOG_FILE_NAME = 'app.log'
    LOG_INI_DIR_NAME = 'config'
    LOG_INI_FILE_NAME = 'logger.ini'
    LOG_INI_QUAL_NAME = 'outputLogging'

    logger = None

    @classmethod
    def get_instance(cls):
        instance: Logger = super().get_instance()
        instance.__init_log()
        return instance

    @classmethod
    def debug(cls, message, *args):
        if args:
            cls.logger.debug(message, args)
        else:
            cls.logger.debug(message)

    @classmethod
    def info(cls, message, *args):
        if args:
            cls.logger.info(message, args)
        else:
            cls.logger.info(message)

    @classmethod
    def warning(cls, message, *args):
        if args:
            cls.logger.warning(message, args)
        else:
            cls.logger.warning(message)

    @classmethod
    def error(cls, message, *args):
        if args:
            cls.logger.error(message, args)
        else:
            cls.logger.error(message)

    @classmethod
    def critical(cls, message, *args):
        if args:
            cls.logger.critical(message, args)
        else:
            cls.logger.critical(message)

    @classmethod
    def __init_log(cls):
        current_path = str(pathlib.Path.cwd())

        log_ini_file_path = current_path + os.sep + cls.LOG_INI_DIR_NAME + os.sep + cls.LOG_INI_FILE_NAME
        logging.config.fileConfig(log_ini_file_path, disable_existing_loggers=False)

        logger = logging.getLogger(cls.LOG_INI_QUAL_NAME)
        logger.setLevel(logging.DEBUG)

        log_file_path = current_path + os.sep + cls.LOG_DIR_NAME + os.sep + cls.LOG_FILE_NAME
        get_handler = logging.FileHandler(log_file_path)
        logger.addHandler(get_handler)

        cls.logger = logger
