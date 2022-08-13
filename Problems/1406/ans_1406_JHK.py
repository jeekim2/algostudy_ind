# https://www.acmicpc.net/problem/1406

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class StringList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.curser = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def put_char(self, data):
        NewNode = Node(data)
        NewNode.next = self.curser.next
        NewNode.prev = self.curser
        self.curser.next.prev = NewNode
        self.curser.next = NewNode
        self.curser = NewNode
        self.size += 1

    def del_char(self):
        if self.curser == self.head:
            return
        self.curser.next.prev = self.curser.prev
        self.curser.prev.next = self.curser.next
        self.curser = self.curser.prev
        self.size -= 1

    def move_left(self):
        if self.curser != self.head:
            self.curser = self.curser.prev

    def move_right(self):
        if self.curser.next == self.tail:
            return
        self.curser = self.curser.next

    def print(self):
        current = self.head.next
        while current != self.tail:
            print(current.data, end="")
            current = current.next
        print()


def solve():
    input = sys.stdin.readline
    InputStr = input().rstrip()
    N = int(input())
    strList = StringList()
    for c in InputStr:
        strList.put_char(c)
    for _ in range(N):
        cmd = input().rstrip()
        if cmd[0] == "L":
            strList.move_left()
            continue
        if cmd[0] == "D":
            strList.move_right()
            continue
        if cmd[0] == "B":
            strList.del_char()
            continue
        if cmd[0] == "P":
            strList.put_char(cmd[2])
            continue
    strList.print()
    return


if __name__ == "__main__":
    solve()
