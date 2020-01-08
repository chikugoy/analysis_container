#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Lock


class Singleton:

    __unique_instance = None
    __lock = Lock()  # クラスロック

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls.__unique_instance:
            with cls.__lock:
                if not cls.__unique_instance:
                    cls.__unique_instance = cls.__internal_new__()
        return cls.__unique_instance
