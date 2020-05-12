#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('../../')
from logic.abstract_interface import AbstractInterface


class ISample2Output(AbstractInterface):

    sample2_attr1: str
    sample2_attr2: float

    def __init__(self):
        super().__init__()
        pass

