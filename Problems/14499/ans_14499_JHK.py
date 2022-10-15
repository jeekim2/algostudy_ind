# https://www.acmicpc.net/problem/14499

import sys


class Dice:
    def __init__(self):
        self.top = 0
        self.bottom = 0
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0

    def roll_up(self):
        temp = self.up
        self.up = self.top
        self.top = self.down
        self.down = self.bottom
        self.bottom = temp

    def roll_down(self):
        temp = self.up
        self.up = self.bottom
        self.bottom = self.down
        self.down = self.top
        self.top = temp

    def roll_left(self):
        temp = self.left
        self.left = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = temp

    def roll_right(self):
        temp = self.right
        self.right = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = temp

    def roll(self, dir, val):
        if dir == 1:
            self.roll_right()
        elif dir == 2:
            self.roll_left()
        elif dir == 3:
            self.roll_up()
        else:
            self.roll_down()
        if val == 0:
            return self.top, self.bottom
        else:
            self.bottom = val
            return self.top, 0


def solve():
    N, M, y, x, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    cmd = list(map(int, input().split()))
    dx = [0, 1, -1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    dice = Dice()
    for c in cmd:
        if 0 <= x + dx[c] < M and 0 <= y + dy[c] < N:
            x += dx[c]
            y += dy[c]
            t, b = dice.roll(c, grid[y][x])
            grid[y][x] = b
            print(t)

    return


if __name__ == "__main__":
    solve()
