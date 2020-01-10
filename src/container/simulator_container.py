#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('./')
from .logic_dict import LogicDict
from .abstract_container import AbstractContainer

sys.path.append('../')
from logic.abstract_interface import AbstractInterface
from logic.abstract_logic import AbstractLogic
from logic.sample1.sample1_logic import Sample1Logic
from logic.sample1.interface.i_sample1_input import ISample1Input
from logic.sample1.interface.i_sample1_output import ISample1Output


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
            if not self.__logic_dict.validateLogicExecDict():
                self._logger.error('logic_dict validation return False')
                return False

            if not self.execute_logic_dict(self.__logic_dict.logic_exec_dict):
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

    def execute_logic_dict(self, logic_exec_dict: dict):
        """logic execute
        
        Args:
            logic_exec_dict (dict): 実行対象ロジックdict
        """        
        for logic_dict in logic_exec_dict:
            input_class_name = logic_dict[LogicDict.LOGIC_EXEC_INPUT_KEY]
            input_class = globals()[input_class_name]
            input_class_instance: AbstractInterface = input_class()

            output_class_name = logic_dict[LogicDict.LOGIC_EXEC_OUTPUT_KEY]
            output_class = globals()[output_class_name]
            output_class_instance: AbstractInterface = output_class()

            logic_class_name = logic_dict[LogicDict.LOGIC_EXEC_KEY]
            logic_class = globals()[logic_class_name]
            logic_class_instance: AbstractLogic = logic_class(
                input_class_instance, output_class_instance)

            self._logger.debug('logic start >>>>>>>>>>>')
            self._logger.debug('logic:' + logic_class_name + ' input:' + input_class_name + ' output:' + output_class_name)

            if logic_class_instance.execute() is False:
                self._logger.error('logic execute fail')
                return False
            else:
                self._logger.debug('logic execute success')

            self._logger.debug('logic end  <<<<<<<<<<<')

        return True
