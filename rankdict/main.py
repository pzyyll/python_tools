# -*- coding:utf-8 -*-
# @Date: "2021-07-14"
# @Description: 排行数据Dict

import sys
import random
from typing import Hashable

SKIPLIST_P = 0.25
MAX_LEVEL = 32


def skRandomLevel():
    lvl = 1
    while(random.random() < SKIPLIST_P and lvl < MAX_LEVEL):
        lvl += 1
    return lvl


class SkipListLevel(object):
    def __init__(self):
        super(SkipListLevel, self).__init__()
        self.forward = None
        self.span = 0


class SkipListNode(object):
    def __init__(self, level, value):
        super(SkipListNode, self).__init__()
        self.value = value
        self.backward = None
        self.levels = [SkipListLevel() for _ in level]


class SkipList(object):
    def __init__(self):
        super(SkipList, self).__init__()
        self._head = SkipListNode(MAX_LEVEL, None)
        self._tail = None
        self._lenth = 0
        self._level = 0


class RankDict(object):
    def __init__(self):
        super(RankDict, self).__init__()

    def insert(self, searchKey, value):
        '''
        @param k : 可重复
        @param v : 不可重复
        '''
        if not Hashable(searchKey):
            raise KeyError('@key must be hashable.')
        pass

    def update(self, k, v):
        pass

    def rank(self, k):
        pass

    def rankByVal(self, val):
        pass

    def range(self, start, stop):
        pass

    def rangeByVal(self, start, stop):
        pass

if __name__ == '__main__':
    cnt = 1000000
    sd = {}
    for _ in range(cnt):
        r = skRandomLevel()
        if r not in sd:
            sd[r] = 1
        else:
            sd[r] += 1
    print(sd)
    for k, v in sd.items():
        sd[k] = v*1.0/cnt

    print(sd)