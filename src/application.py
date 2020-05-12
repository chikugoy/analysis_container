#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
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

 # 分析結果整形・出力  ****************************************
output = container.get_logic_output()
output_model_infos: dict = {
    'sample2_attr1': output.sample2_attr1,
    'sample2_attr2': output.sample2_attr2
}
df = pd.DataFrame(output_model_infos,index=['index',])
print(df)