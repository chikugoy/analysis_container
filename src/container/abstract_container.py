#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from abc import ABCMeta, abstractmethod

sys.path.append('../')
from extention.logger import Logger


class AbstractContainer(metaclass=ABCMeta):
    """コンテナ基底クラス
       ここでのコンテナはpython的なlistやdictではなく
       ロジック実行用の箱の事

    Args:
        metaclass ([type], optional): [description]. Defaults to ABCMeta.
    """

    _logger: Logger = Logger.get_instance()

    def __init__(self):
        """constructor
        """
        pass

    @abstractmethod
    def execute(self):
        pass
