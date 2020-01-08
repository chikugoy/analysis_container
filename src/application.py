#!/usr/bin/env python
# -*- coding: utf-8 -*-

from container.simulator_container import SimulatorContainer
from container.logic_dict import LogicDict
from logic.sample.sample_logic import SampleLogic
from logic.sample.interface.i_sample_input import ISampleInput
from logic.sample.interface.i_sample_output import ISampleOutput

logic_dict: LogicDict = LogicDict([{
    LogicDict.LOGIC_EXEC_KEY: 'SampleLogic',
    LogicDict.LOGIC_EXEC_INPUT_KEY: 'ISampleInput',
    LogicDict.LOGIC_EXEC_OUTPUT_KEY: 'ISampleOutput',
}])
container = SimulatorContainer(logic_dict)
container.execute()
