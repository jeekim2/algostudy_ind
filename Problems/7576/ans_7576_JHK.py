# https://www.acmicpc.net/problem/7576

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
        data = self.head.next.data
        self.head.next = self.head.next.next
        self.size -= 1
        return data


def ripe_around(baseIdx, Tomato: list, N, M, buffer_queue: Queue):
    x, y = baseIdx % M, baseIdx // M
    ripeResult = False
    if x > 0:
        tarIdx = y * M + x - 1
        if Tomato[tarIdx] == 0:
            Tomato[tarIdx] = 1
            buffer_queue.enqueue(tarIdx)
            ripeResult = True
    if x < M - 1:
        tarIdx = y * M + x + 1
        if Tomato[tarIdx] == 0:
            Tomato[tarIdx] = 1
            buffer_queue.enqueue(tarIdx)
            ripeResult = True
    if y > 0:
        tarIdx = (y - 1) * M + x
        if Tomato[tarIdx] == 0:
            Tomato[tarIdx] = 1
            buffer_queue.enqueue(tarIdx)
            ripeResult = True
    if y < N - 1:
        tarIdx = (y + 1) * M + x
        if Tomato[tarIdx] == 0:
            Tomato[tarIdx] = 1
            buffer_queue.enqueue(tarIdx)
            ripeResult = True

    return ripeResult


def solve():
    input = sys.stdin.readline
    M, N = map(int, input().split())
    Tomato = []
    for _ in range(N):
        Tomato += list(map(int, input().split()))
    queue = Queue()
    buffer_queue = Queue()
    for i, v in enumerate(Tomato):
        if v == 1:
            queue.enqueue(i)

    cnt = 0
    ripeResult = False
    while queue.size > 0:
        if ripe_around(queue.dequeue(), Tomato, N, M, buffer_queue):
            ripeResult = True
        if queue.size == 0 and ripeResult:
            queue, buffer_queue = buffer_queue, queue
            cnt += 1
            ripeResult = False

    for v in Tomato:
        if v == 0:
            print(-1)
            return
    print(cnt)
    return


if __name__ == "__main__":
    solve()
