#!/usr/bin/env python
# -*- coding: utf-8 -*-

from container.simulator_container import SimulatorContainer
from container.logic_dict import LogicDict

logic_dict: LogicDict = LogicDict(
    [
        {
            LogicDict.LOGIC_EXEC_KEY: 'Sample1Logic',
            LogicDict.LOGIC_EXEC_INPUT_KEY: '',
            LogicDict.LOGIC_EXEC_OUTPUT_KEY: 'ISample1Output',
        },
        {
            LogicDict.LOGIC_EXEC_KEY: 'Sample2Logic',
            LogicDict.LOGIC_EXEC_INPUT_KEY: 'ISample1Output',
            LogicDict.LOGIC_EXEC_OUTPUT_KEY: 'ISample2Output',
        }
    ]
)

container = SimulatorContainer(logic_dict)
container.execute()
