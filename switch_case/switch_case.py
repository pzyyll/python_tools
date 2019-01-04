# -*- coding:utf-8 -*-

from functools import wraps


class SwitchCase(object):
    def __init__(self):
        self.__funcs = {}

    def Case(self, key):

        def Decorate(func):

            self.__funcs[key] = func
            #print(self.__funcs)
            return func

        return Decorate

    def Default(self, *args, **kwargs):
        raise KeyError("SwitchCase key not exist.")

    def Do(self, key):
        if key not in self.__funcs:
            return self.Default
        return self.__funcs[key]

def FuncBig():

    switch_case = SwitchCase()

    @switch_case.Case("yes")
    def Func(str):
        print("Func: " + str)

    @switch_case.Case("no")
    def Func2(str):
        print("Func2: " + str)

    switch_case.Do("no2")('123')

FuncBig()