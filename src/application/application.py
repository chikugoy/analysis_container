#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

print("os.getcwd() -> ",os.getcwd())

sys.path.append(os.getcwd())
print(sys.path)

from ..container.simulator_container import SimulatorContainer
from ..container.logic_dict import LogicDict
from ..logic.sample.sample_logic import SampleLogic
from ..logic.sample.interface.i_sample_input import ISampleInput
from ..logic.sample.interface.i_sample_output import ISampleOutput

logic_dict: LogicDict = LogicDict([{
    LogicDict.LOGIC_EXEC_KEY: 'SampleLogic',
    LogicDict.LOGIC_EXEC_INPUT_KEY: 'ISampleInput',
    LogicDict.LOGIC_EXEC_OUTPUT_KEY: 'ISampleOutput',
}])
container = SimulatorContainer(logic_dict)
if container.execute() is False:
    raise Exception('コンテナの実行に失敗しました')
