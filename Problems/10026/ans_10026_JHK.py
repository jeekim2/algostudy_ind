# https://www.acmicpc.net/problem/10026

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
        self.tail.data = data
        NewNode = Node(None)
        self.tail.next = NewNode
        self.tail = NewNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        TarNode = self.head.next
        data = TarNode.data
        self.head.next = self.head.next.next
        self.size -= 1
        del TarNode
        return data

    def is_exist(self):
        return self.size > 0


def count_normal_area(ColorMap, N):
    queue = Queue()
    is_not_visited = [True] * len(ColorMap)
    i = 0
    cnt = 0
    while i < len(ColorMap):
        if is_not_visited[i]:
            cnt += 1
            queue.enqueue(i)
            is_not_visited[i] = False
            DefColor = ColorMap[i]
            while queue.is_exist():
                idx = queue.dequeue()
                x, y = idx % N, idx // N
                if x > 0:
                    tarIdx = (x - 1) + y * N
                    if is_not_visited[tarIdx] and ColorMap[tarIdx] == DefColor:
                        queue.enqueue(tarIdx)
                        is_not_visited[tarIdx] = False
                if x < N - 1:
                    tarIdx = (x + 1) + y * N
                    if is_not_visited[tarIdx] and ColorMap[tarIdx] == DefColor:
                        queue.enqueue(tarIdx)
                        is_not_visited[tarIdx] = False
                if y > 0:
                    tarIdx = x + (y - 1) * N
                    if is_not_visited[tarIdx] and ColorMap[tarIdx] == DefColor:
                        queue.enqueue(tarIdx)
                        is_not_visited[tarIdx] = False
                if y < N - 1:
                    tarIdx = x + (y + 1) * N
                    if is_not_visited[tarIdx] and ColorMap[tarIdx] == DefColor:
                        queue.enqueue(tarIdx)
                        is_not_visited[tarIdx] = False
        else:
            i += 1
    return cnt


def count_color_weak_area(ColorMap, N):
    queue = Queue()
    is_not_visited = [True] * len(ColorMap)
    i = 0
    cnt = 0
    while i < len(ColorMap):
        if is_not_visited[i]:
            cnt += 1
            queue.enqueue(i)
            is_not_visited[i] = False
            DefColor = ColorMap[i] > 0
            while queue.is_exist():
                idx = queue.dequeue()
                x, y = idx % N, idx // N
                if x > 0:
                    tarIdx = (x - 1) + y * N
                    if is_not_visited[tarIdx] and (ColorMap[tarIdx] > 0) == DefColor:
                        queue.enqueue(tarIdx)
                        is_not_visited[tarIdx] = False
                if x < N - 1:
                    tarIdx = (x + 1) + y * N
                    if is_not_visited[tarIdx] and (ColorMap[tarIdx] > 0) == DefColor:
                        queue.enqueue(tarIdx)
                        is_not_visited[tarIdx] = False
                if y > 0:
                    tarIdx = x + (y - 1) * N
                    if is_not_visited[tarIdx] and (ColorMap[tarIdx] > 0) == DefColor:
                        queue.enqueue(tarIdx)
                        is_not_visited[tarIdx] = False
                if y < N - 1:
                    tarIdx = x + (y + 1) * N
                    if is_not_visited[tarIdx] and (ColorMap[tarIdx] > 0) == DefColor:
                        queue.enqueue(tarIdx)
                        is_not_visited[tarIdx] = False
        else:
            i += 1
    return cnt


def solve():
    input = sys.stdin.readline
    N = int(input())
    ColorMap = []
    for _ in range(N):
        tempStr = input().rstrip()
        for c in tempStr:
            if c == "R":
                ColorMap.append(1)
            elif c == "G":
                ColorMap.append(2)
            else:
                ColorMap.append(0)
    print(count_normal_area(ColorMap, N), end=" ")
    print(count_color_weak_area(ColorMap, N))
    return


if __name__ == "__main__":
    solve()
