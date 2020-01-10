#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('../../')
from logic.abstract_interface import AbstractInterface


class ISample1Output(AbstractInterface):

    sample1_attr1: str
    sample1_attr2: int
    sample1_attr3: float

    def __init__(self):
        super().__init__()
        pass

