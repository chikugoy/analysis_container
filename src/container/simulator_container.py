#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('./')
from .logic_dict import LogicDict
from .abstract_container import AbstractContainer

sys.path.append('../')
from logic.abstract_interface import AbstractInterface
from logic.abstract_logic import AbstractLogic


class SimulatorContainer(AbstractContainer):
    """Simulator Container

    Args:
        AbstractContainer (AbstractContainer): AbstractContainer継承
    """

    def __init__(self, logic_dict: LogicDict, options={}):
        """constructor

        Args:
            AbstractContainer ([type]): [description]
            logic_dict (LogicDict): [description]
            options ([type]): [description]
        """
        self.__logic_dict: LogicDict = logic_dict

    def execute(self):
        """container execute

        Returns:
            bool: True: execute success False: execute fail
        """
        self._logger.debug('container execute start >>>>>>>>>>>>>>>>>>>')
        try:
            self.__logic_dict.set_logger(self._logger)
            if not self.__logic_dict.validate_logic_exec_dict():
                self._logger.error('logic_dict validation return False')
                return False

            if not self.__execute_logic_dict(self.__logic_dict.get_logic_exec_class_dict()):
                self._logger.error('execute logic_exec_dict return False')
                return False

        except Exception as e:
            self._logger.error('container execute catch Exception:', e)
            return False
        else:
            self._logger.debug('container execute success')
            return True
        finally:
            self._logger.debug('container execute end  <<<<<<<<<<<<<<<<<<<<')

    def __execute_logic_dict(self, logic_exec_instance_dict: dict):
        """logic execute

        Args:
            logic_exec_dict (dict): 実行対象ロジックdict
        """
        for logic_exec_instance_list in logic_exec_instance_dict:
            logic_class = logic_exec_instance_list[LogicDict.LOGIC_EXEC_KEY]
            logic_input_instance = logic_exec_instance_list[LogicDict.LOGIC_EXEC_INPUT_KEY]()
            logic_output_instance = logic_exec_instance_list[LogicDict.LOGIC_EXEC_OUTPUT_KEY]()
            logic_instance: AbstractLogic = logic_class(
                logic_input_instance, logic_output_instance)

            self._logger.debug('logic start >>>>>>>>>>>')
            self._logger.debug('logic:' + logic_instance.__class__.__name__ +
                               ' input:' + logic_input_instance.__class__.__name__ +
                               ' output:' + logic_output_instance.__class__.__name__)

            if logic_instance.execute() is False:
                self._logger.error('logic execute fail')
                return False
            else:
                self._logger.debug('logic execute success')

            self._logger.debug('logic end  <<<<<<<<<<<')

        return True
