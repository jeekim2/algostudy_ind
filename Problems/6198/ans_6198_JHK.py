# https://www.acmicpc.net/problem/6198

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def push(self, data):
        Dummy = Node(None)
        self.head.data = data
        Prev = self.head
        self.head = Dummy
        Dummy.next = Prev
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        data = self.head.next.data
        self.size -= 1
        self.head.next = self.head.next.next
        return data

    def top(self):
        if self.size == 0:
            return -1
        return self.head.next.data


def solve():
    input = sys.stdin.readline
    N = int(input())
    Building = [int(input()) for _ in range(N)]
    res = 0
    stack = Stack()
    for v in Building:
        while stack.size != 0 and stack.top() <= v:
            stack.pop()
        res += stack.size
        stack.push(v)
    print(res)
    return


if __name__ == "__main__":
    solve()
