# https://www.acmicpc.net/problem/10216

import sys


class Base:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.link = []


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
        TarNode = self.tail.prev
        self.tail.prev = TarNode.prev
        TarNode.prev.next = self.tail
        self.size -= 1
        return TarNode.data


def is_connected(A, B):
    if ((A.x - B.x) ** 2) + ((A.y - B.y) ** 2) <= (A.r + B.r) ** 2:
        return True
    return False


def solve():
    input = sys.stdin.readline
    T = int(input())
    res = []
    for _ in range(T):
        N = int(input())
        Bases = []
        isVisited = [False] * N
        connection = [[False] * N for _ in range(N)]
        for _ in range(N):
            x, y, r = map(int, input().split())
            Bases.append(Base(x, y, r))
        for i in range(N):
            for j in range(i + 1, N):
                if is_connected(Bases[i], Bases[j]):
                    connection[i][j], connection[j][i] = True, True
        q = Queue()
        cnt = 0
        for i in range(N):
            if not isVisited[i]:
                q.enqueue(i)
                isVisited[i] = True
                cnt += 1
                while q.size != 0:
                    i = q.dequeue()
                    for j, v in enumerate(connection[i]):
                        if v and not isVisited[j]:
                            q.enqueue(j)
                            isVisited[j] = True
        res.append(cnt)
    for v in res:
        print(v)
    return


if __name__ == "__main__":
    solve()
