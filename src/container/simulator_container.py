#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('./')
from .logic_dict import LogicDict
from .abstract_container import AbstractContainer

sys.path.append('../')
from logic.abstract_interface import AbstractInterface
from logic.abstract_logic import AbstractLogic
from extention.logger import Logger


class SimulatorContainer(AbstractContainer):
    logger: Logger = Logger.get_instance()

    def __init__(self, logic_dict: LogicDict, options={}):
        """constructor

        Args:
            AbstractContainer ([type]): [description]
            logic_dict (LogicDict): [description]
            options ([type]): [description]
        """
        self.__logic_dict: LogicDict = logic_dict

    def execute(self):
        try:
            # ロジックリストのバリデーション
            if not self.__logic_dict.validateLogicExecDict():
                return False

            # ロジックリストの実行
            if not self.execute_logic_dict(self.__logic_dict):
                return False

        except Exception as e:
            logger.error('catch Exception:', e)
        else:
            print('finish (no error)')
        finally:
            print('all finish')

    def execute_logic_dict(self, logic_dict: dict):
        for index in logic_dict:
            input_class_name = logic_dict[index][LogicDict.LOGIC_EXEC_INPUT_KEY]
            input_class = globals()[input_class_name]
            input_class_instance: AbstractInterface = input_class()

            output_class_name = logic_dict[index][LogicDict.LOGIC_EXEC_OUTPUT_KEY]
            output_class = globals()[output_class_name]
            output_class_instance: AbstractInterface = output_class()

            logic_class_name = logic_dict[index][LogicDict.LOGIC_EXEC_KEY]
            logic_class = globals()[logic_class_name]
            logic_class_instance: AbstractLogic = logic_class(
                input_class_instance, output_class_instance)

            logic_class_instance.execute()
