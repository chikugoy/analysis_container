#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('../')
from logic.abstract_logic import AbstractLogic
from logic.abstract_interface import AbstractInterface


class Sample2Logic(AbstractLogic):

    def __init__(self, inputValue: AbstractInterface, output: AbstractInterface):
        super().__init__(inputValue, output)

    def execute(self) -> bool:
        self._logger.debug('sample2 logic execute!!')
        self.output = self._output
        return True
