# https://www.acmicpc.net/problem/16236

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def enqueue(self, data):
        NewNode = Node(data)
        NewNode.next = self.head.next
        NewNode.prev = self.head
        self.head.next = NewNode
        NewNode.next.prev = NewNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        Target = self.tail.prev
        data = Target.data
        self.tail.prev = Target.prev
        Target.prev.next = self.tail
        self.size -= 1
        return data


class Shark:
    def __init__(self, pos, grid):
        self.grid = grid
        self.pos = pos
        self.size = 2
        self.eatenCnt = 0

    def eat(self, pos):
        self.grid[self.pos] = 0
        self.pos = pos
        self.grid[self.pos] = 9
        self.eatenCnt += 1
        if self.eatenCnt == self.size:
            self.size += 1
            self.eatenCnt = 0


def SearchAround(p, beforeTime, sharkSize, grid, visitTime, N):
    x, y = p % N, p // N
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    res = []
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            newP = x + dx[i] + (y + dy[i]) * N
            if visitTime[newP] < 0 and grid[newP] <= sharkSize:
                res.append(newP)
                visitTime[newP] = beforeTime + 1
    return res


def solve():
    input = sys.stdin.readline
    N = int(input())
    grid = []
    for _ in range(N):
        grid += list(map(int, input().split()))
    for i, v in enumerate(grid):
        if v == 9:
            s = Shark(i, grid)
            break
    timer = 0
    while True:
        FirstQ = Queue()
        SecondQ = Queue()
        visitTime = [-1] * len(grid)
        visitTime[s.pos] = 0
        FirstQ.enqueue(s.pos)
        fish_found = False
        MinIdx = N * N
        while not fish_found:
            while FirstQ.size != 0:
                p = FirstQ.dequeue()
                beforTime = visitTime[p]
                for i in SearchAround(p, beforTime, s.size, grid, visitTime, N):
                    if grid[i] != 0 and s.size > grid[i]:
                        fish_found = True
                        MinIdx = min(MinIdx, i)
                    SecondQ.enqueue(i)
            if SecondQ.size == 0:
                print(timer)
                return
            FirstQ, SecondQ = SecondQ, FirstQ
        s.eat(MinIdx)
        timer += visitTime[MinIdx]
    return


if __name__ == "__main__":
    solve()
