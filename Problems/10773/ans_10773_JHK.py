# https://www.acmicpc.net/problem/10773

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head.next
        NewNode.prev = self.head
        self.head.next = NewNode
        NewNode.next.prev = NewNode
        self.size += 1

    def pop(self):
        if self.size == 0:
            return 0
        TarNode = self.head.next
        self.head.next = TarNode.next
        TarNode.next.prev = self.head
        self.size -= 1
        return TarNode.data


class NumList:
    def __init__(self):
        self.sum = 0
        self.stack = Stack()

    def WriteNum(self, data):
        self.sum += data
        self.stack.push(data)

    def DelNum(self):
        self.sum -= self.stack.pop()

    def getSum(self):
        return self.sum


def solve():
    input = sys.stdin.readline
    K = int(input())
    numlist = NumList()
    for _ in range(K):
        num = int(input())
        if num == 0:
            numlist.DelNum()
        else:
            numlist.WriteNum(num)
    print(numlist.getSum())
    return


if __name__ == "__main__":
    solve()
