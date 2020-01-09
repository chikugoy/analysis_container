#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('../')
from logic.abstract_logic import AbstractLogic
from logic.abstract_interface import AbstractInterface


class LogicDict:
    """ロジック実行用のキーバリュー格納用クラス

       格納以外に検証機能もあり
    """

    # ロジック実行用のキーバリューのキー
    LOGIC_EXEC_KEY = 'logic'            # 実行対象logicクラス用のキー
    LOGIC_EXEC_INPUT_KEY = 'input'      # 実行対象logicのインプットインターフェイス用のキー
    LOGIC_EXEC_OUTPUT_KEY = 'output'    # 実行対象logicのアウトプットインターフェイス用のキー
    LOGIC_EXEC_REQUIRED_KEY: tuple = (LOGIC_EXEC_KEY, LOGIC_EXEC_INPUT_KEY, LOGIC_EXEC_OUTPUT_KEY)

    # ロジック実行用のキーバリューのキーの数（固定）
    LOGIC_EXEC_KEY_LENGTH = 3

    def __init__(self, logic_exec_dict: dict):
        """コンストラクタ

        Args:
            logic_exec_dict (dict): ロジック実行用のキーバリュー
            logic_exec_dictは下記の形式で格納されている
            [{ 'logic': LogicClass, 'input': InputClass, 'output': OutputClass}]
        """
        self.logic_exec_dict: dict = logic_exec_dict

    def validateLogicExecDict(self):
        """ロジック実行用のキーバリューを検証する

        Returns:
            bool: true:検証OK false:検証NG
        """

        if not self.logic_exec_dict:
            return False

        for logic_exec_list in self.logic_exec_dict:
            logic_exec_keys: list = []
            for logic_exec_key in logic_exec_list:
                logic_exec_keys.append(logic_exec_key)

            # 必須キーのみが含まれているか検証
            if self.validateOnlyRequireKeys(logic_exec_keys) is False:
                return False

            # ロジック実行用のキーに対する値が設定されているか、また、特定の型を継承しているか検証
            if self.validateRequireValuesAndType(self.logic_exec_dict) is False:
                return False

    def validateOnlyRequireKeys(self, logic_exec_keys: list):
        """必須キーのみが含まれているか検証
        
        Args:
            logic_exec_keys (list): ロジック実行用のキーバリュー
        
        Returns:
            bool: true:検証OK false:検証NG
        """        
        if not logic_exec_keys:
            return False
        elif len(logic_exec_keys) != self.LOGIC_EXEC_KEY_LENGTH:
            return False

        required_keys: list = list(self.LOGIC_EXEC_REQUIRED_KEY)

        for index, key in enumerate(logic_exec_keys):
            if not key in required_keys:
                return False

            del required_keys[index]

        if not required_keys:
            return True

        return False

    def validateRequireValuesAndType(self, logic_exec_dict: dict):
        """ロジック実行用のキーに対する値が設定されているか
           また特定の型を継承しているか検証
        
        Args:
            logic_exec_dict (dict): [description]
        
        Returns:
            bool: true:検証OK false:検証NG
        """        
        for logic_exec_list in logic_exec_dict:
            if not logic_exec_list[self.LOGIC_EXEC_KEY]:
                return False
            elif issubclass(logic_exec_list[self.LOGIC_EXEC_KEY]. AbstractLogic):
                return False

            if not logic_exec_list[self.LOGIC_EXEC_INPUT_KEY]:
                return False
            elif issubclass(logic_exec_list[self.LOGIC_EXEC_INPUT_KEY]. AbstractInterface):
                return False

            if not logic_exec_list[self.LOGIC_EXEC_OUTPUT_KEY]:
                return False
            elif issubclass(logic_exec_list[self.LOGIC_EXEC_OUTPUT_KEY]. AbstractInterface):
                return False
