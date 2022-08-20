# https://www.acmicpc.net/problem/2573

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        return


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.size = 0

    def enqueue(self, data):
        dummy = Node(None)
        self.tail.data = data
        self.tail.next = dummy
        self.tail = dummy
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        data = self.head.next.data
        self.head.next = self.head.next.next
        self.size -= 1
        return data


def checkSea(x):
    return x == 0


def visit_island(i, N, M, IsVisited):
    return


def melt_iceberg(N, M, Iceberg):
    MeltCntSet = [0] * len(Iceberg)
    IsVisited = list(map(checkSea, Iceberg))
    VisitingQueue = Queue()
    IslandCnt = 0
    for i, v in enumerate(IsVisited):
        if not v:
            IslandCnt += 1
            if IslandCnt > 1:
                return IslandCnt
            VisitingQueue.enqueue(i)
            IsVisited[i] = True
            while VisitingQueue.size > 0:
                base = VisitingQueue.dequeue()
                baseX, baseY = base % M, base // M
                meltCnt = 0
                if baseX > 0:
                    tempIdx = base - 1
                    if not IsVisited[tempIdx]:
                        VisitingQueue.enqueue(tempIdx)
                        IsVisited[tempIdx] = True
                    if Iceberg[tempIdx] == 0:
                        meltCnt += 1
                if baseX < M - 1:
                    tempIdx = base + 1
                    if not IsVisited[tempIdx]:
                        VisitingQueue.enqueue(tempIdx)
                        IsVisited[tempIdx] = True
                    if Iceberg[tempIdx] == 0:
                        meltCnt += 1
                if baseY > 0:
                    tempIdx = base - M
                    if not IsVisited[tempIdx]:
                        VisitingQueue.enqueue(tempIdx)
                        IsVisited[tempIdx] = True
                    if Iceberg[tempIdx] == 0:
                        meltCnt += 1
                if baseY < N - 1:
                    tempIdx = base + M
                    if not IsVisited[tempIdx]:
                        VisitingQueue.enqueue(tempIdx)
                        IsVisited[tempIdx] = True
                    if Iceberg[tempIdx] == 0:
                        meltCnt += 1
                MeltCntSet[base] = meltCnt
            for i in range(N * M):
                if MeltCntSet[i] > Iceberg[i]:
                    Iceberg[i] = 0
                else:
                    Iceberg[i] -= MeltCntSet[i]
    return IslandCnt


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Iceberg = []
    for _ in range(N):
        Iceberg += list(map(int, input().split()))

    ResYear = 0
    while True:
        res = melt_iceberg(N, M, Iceberg)
        if res == 1:
            ResYear += 1
        elif res == 0:
            print(0)
            return
        else:
            print(ResYear)
            return


if __name__ == "__main__":
    solve()
