#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class AbstractContainer(metaclass=ABCMeta):
    """コンテナ基底クラス
       ここでのコンテナはpython的なlistやdictではなく
       ロジック実行用の箱の事

    Args:
        metaclass ([type], optional): [description]. Defaults to ABCMeta.
    """

    def __init__(self):
        """constructor
        """
        pass

    @abstractmethod
    def execute(self):
        pass
