# https://www.acmicpc.net/problem/17952

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
        NewNode.prev = self.tail.prev
        NewNode.next = self.tail
        self.tail.prev.next = NewNode
        self.tail.prev = NewNode
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1, 0
        TarNode = self.tail.prev
        data = TarNode.data
        self.tail.prev = TarNode.prev
        TarNode.prev.next = self.tail
        self.size -= 1
        return data


class Homework:
    def __init__(self):
        self.HwStack = Stack()

    def DayOver(self):
        time, score = self.HwStack.pop()
        if time > 1:
            self.HwStack.push([time - 1, score])
            return 0
        return score

    def NewHomework(self, time, score):
        self.HwStack.push([time, score])
        retScore = self.DayOver()
        return retScore


def solve():
    input = sys.stdin.readline
    N = int(input())
    HwStack = Homework()
    res = 0
    for _ in range(N):
        cmd = input().rstrip()
        if cmd[0] == "0":
            res += HwStack.DayOver()
        else:
            __, score, time = map(int, cmd.split())

            res += HwStack.NewHomework(time, score)
    print(res)
    return


if __name__ == "__main__":
    solve()
