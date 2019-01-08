# -*- coding:utf-8 -*-
# 利用装饰器和所谓的表驱动去简单封装一个 switch case 逻辑，
# 不知道这样是否更加复杂化逻辑，不符合一个懒惰的 pythonic

from functools import wraps

import sys

CUECALLBACK = {}

class SwitchCase(object):
    def __init__(self):
        self.__funcs = {}
        self.__default = None

    def Case(self, key):

        def Decorate(func):
            self.__funcs[key] = func
            return func

        return Decorate

    def Default(self, func):

        self.__default = func

        return func

    def Do(self, key):
        if key in self.__funcs:
            return self.__funcs[key]
        elif self.__default != None:
            return self.__default
        else:
            raise KeyError("SwitchCase key not exist.")



switch_case = SwitchCase()

@switch_case.Case("yes")
def Func(str):
    print("Func: " + str)

@switch_case.Case("no")
def Func2(str):
    print("Func2: " + str)

@switch_case.Case(1)
def Func3(str):
    print("Func3: " + str)

switch_case.Do("no")("xxx")