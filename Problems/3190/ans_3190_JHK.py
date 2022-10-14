# https://www.acmicpc.net/problem/3190

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Snake:
    def __init__(self, N, grid):
        self.N = N
        self.Grid = grid
        self.dx = [0, -1, 0, 1]
        self.dy = [-1, 0, 1, 0]
        self.direction = 3
        self.head = Node(0)
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head

    def turn(self, d):
        if d == 1:
            # turn left (CCW)
            self.direction += 1
            if self.direction > 3:
                self.direction -= 4
        else:
            if self.direction == 0:
                self.direction = 3
            else:
                self.direction -= 1

    def go(self):
        pos = self.head.data
        x, y = pos % self.N, pos // self.N
        x = x + self.dx[self.direction]
        y = y + self.dy[self.direction]
        if 0 <= x < self.N and 0 <= y < self.N:
            pos = y * self.N + x
            if self.Grid[pos] == 1:
                # eat apple
                self.Grid[pos] = 2
                NewHead = Node(pos)
                NewHead.next = self.head
                self.head.prev = NewHead
                self.head = NewHead
            elif self.Grid[pos] == 0:
                # go in empty space
                self.Grid[pos] = 2
                NewHead = Node(pos)
                NewHead.next = self.head
                self.head.prev = NewHead
                self.head = NewHead
                self.Grid[self.tail.data] = 0
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                # colapse body
                return False

            return True
        # colapse wall
        return False


def solve():
    input = sys.stdin.readline
    N = int(input())
    Grid = [0] * (N * N)

    K = int(input())
    Apple = []
    for _ in range(K):
        y, x = map(int, input().split())
        y -= 1
        x -= 1
        Grid[y * N + x] = 1
    L = int(input())
    cmd = []
    for _ in range(L):
        t, d = input().split()
        tt = int(t)
        if d == "L":
            cmd.append((tt, 1))
        else:
            cmd.append((tt, 0))

    s = Snake(N, Grid)
    i = 1
    cmdIdx = 0
    Grid[0] = 2
    while True:
        if not s.go():
            print(i)
            return
        if cmdIdx < L:
            if cmd[cmdIdx][0] == i:
                s.turn(cmd[cmdIdx][1])
                cmdIdx += 1
        i += 1


if __name__ == "__main__":
    solve()

# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 2 0 0
# 0 0 0 2 0 0
