#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from abc import ABCMeta, abstractmethod

sys.path.append('./')
from .abstract_interface import AbstractInterface

sys.path.append('../')
from config.config_ini import ConfigIni


class AbstractLogic(metaclass=ABCMeta):

    def __init__(self, inputValue: AbstractInterface, output: AbstractInterface):
        self._input = inputValue
        self._output = output

    @abstractmethod
    def execute(self):
        pass
