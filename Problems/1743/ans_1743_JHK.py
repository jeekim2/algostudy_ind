# https://www.acmicpc.net/problem/1743

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.size = 0

    def enqueue(self, data):
        Dummy = Node(None)
        self.tail.data = data
        self.tail.next = Dummy
        self.tail = Dummy
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        data = self.head.next.data
        self.head.next = self.head.next.next
        self.size -= 1
        return data


def explore_garbage(N, M, i, Garbage):
    queue = Queue()
    cnt = 0
    queue.enqueue(i)
    Garbage[i] = False
    while queue.size > 0:
        v = queue.dequeue()
        cnt += 1
        defr, defc = v // M, v % M
        if defr > 0:
            i = (defr - 1) * M + defc
            if Garbage[i]:
                queue.enqueue(i)
                Garbage[i] = False
        if defr < N - 1:
            i = (defr + 1) * M + defc
            if Garbage[i]:
                queue.enqueue(i)
                Garbage[i] = False
        if defc > 0:
            i = defr * M + defc - 1
            if Garbage[i]:
                queue.enqueue(i)
                Garbage[i] = False
        if defc < M - 1:
            i = defr * M + defc + 1
            if Garbage[i]:
                queue.enqueue(i)
                Garbage[i] = False

    return cnt


def solve():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    Garbage = [False] * (N * M)

    for _ in range(K):
        r, c = map(int, input().split())
        Garbage[c - 1 + (r - 1) * M] = True
    MaxCnt = 0
    for i, v in enumerate(Garbage):
        if v:
            MaxCnt = max(MaxCnt, explore_garbage(N, M, i, Garbage))
    print(MaxCnt)
    return


if __name__ == "__main__":
    solve()
