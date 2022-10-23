# https://www.acmicpc.net/problem/14502

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


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
        TarNode = self.tail.prev
        TarNode.prev.next = self.tail
        self.tail.prev = TarNode.prev
        self.size -= 1
        return TarNode.data


def check_around(Grid, N, M, is_visited, Q, idx):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    x, y = idx % M, idx // M
    cnt = 0
    for i in range(4):
        if 0 <= x + dx[i] < M and 0 <= y + dy[i] < N:
            idx = x + dx[i] + (y + dy[i]) * M
            if Grid[idx] == 0 and not is_visited[idx]:
                is_visited[idx] = True
                Q.enqueue(idx)
                cnt += 1
    return cnt


def get_virus_cnt(Grid, N, M, Virus):
    Q = Queue()
    is_visited = [False] * (N * M)
    cnt = 0
    for v in Virus:
        is_visited[v] = True
        Q.enqueue(v)
    while Q.size != 0:
        cnt += check_around(Grid, N, M, is_visited, Q, Q.dequeue())
    return cnt


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Grid = []
    for _ in range(N):
        Grid += list(map(int, input().split()))
    Virus = []
    MaxEmpty = 0
    for i, v in enumerate(Grid):
        if v == 0:
            MaxEmpty += 1
        elif v == 2:
            Virus.append(i)
    res = 0
    for i in range(N * M):
        if Grid[i] == 0:
            Grid[i] = 1
            for j in range(i + 1, N * M):
                if Grid[j] == 0:
                    Grid[j] = 1
                    for k in range(j + 1, N * M):
                        if Grid[k] == 0:
                            Grid[k] = 1
                            res = max(
                                res, MaxEmpty - get_virus_cnt(Grid, N, M, Virus) - 3
                            )
                            Grid[k] = 0
                    Grid[j] = 0
            Grid[i] = 0
    print(res)
    return


if __name__ == "__main__":
    solve()
