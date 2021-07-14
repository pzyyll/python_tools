# -*- coding:utf-8 -*-
# @Date: "2021-04-01"
# @Description: ranklist


class ListNode(object):
    def __init__(self, data=0):
        super(ListNode, self).__init__()
        self.data = data
        self.next = None

    def __eq__(self, o):
        return self.data == o.data

    def __lt__(self, o):
        return self.data < o.data

    def __gt__(self, o):
        return o < self

    def __le__(self, o):
        return self < o or self == o

    def __ge__(self, o):
        return self > o or self == o


class SortList(object):
    def __init__(self):
        super(SortList, self).__init__()
        self._head = ListNode()
        self._tail_nil = ListNode()

        self._head.next = self._tail_nil

    def isEmpty(self):
        return self._head.next is self._tail_nil

    def insert(self, node, idx=0):
        loopidx = 0
        pre = self._head
        while pre.next is not self._tail_nil:
            if loopidx == idx:
                break
            pre = pre.next
            loopidx += 1
        node.next = pre.next
        pre.next = node

    def insertSort(self, node):
        pre = self._head
        while pre.next is not self._tail_nil:
            if (node < pre.next):
                break
            pre = pre.next
        node.next = pre.next
        pre.next = node

    def remove(self, node):
        delnode = node.next
        node.data = delnode.data
        node.next = delnode.next
        del delnode

    def __repr__(self):
        if self.isEmpty():
            return ''
        repr = ""
        iter = self._head.next
        while iter != self._tail_nil:
            repr += str(iter.data) + '->'
            iter = iter.next
        repr += 'nil'
        return repr


s0 = SortList()

s0.insert(ListNode(1))
node = ListNode(2)
s0.insert(node)
s0.insert(ListNode(3))

s0.remove(node)

print(s0)

node0 = ListNode(4)
node1 = ListNode(2)
node3 = ListNode(1)

s0.insert(node0)
s0.insert(node1)
s0.insert(node3)

print(node0 < node1)
print(node0 > node1)
print(node0 <= node1)
print(node0 >= node1)
print(node0 == node3)
print(node0 == node1)

s1 = SortList()
s1.insertSort(node3)
s1.insertSort(node1)
s1.insertSort(node0)

print(s1)