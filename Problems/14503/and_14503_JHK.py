# https://www.acmicpc.net/problem/14503

import sys


class Robot:
    def __init__(self, x, y, d, grid, N, M):
        self.N = N
        self.M = M
        self.grid = grid
        self.x = x
        self.y = y
        self.dir = d
        self.dx = [0, 1, 0, -1]
        self.dy = [-1, 0, 1, 0]
        self.cleanCnt = 0

    def turnleft(self):
        self.dir += 3
        self.dir %= 4

    def moveFront(self):
        self.x += self.dx[self.dir]
        self.y += self.dy[self.dir]

    def moveBack(self):
        self.x -= self.dx[self.dir]
        self.y -= self.dy[self.dir]

    def clean(self):
        if self.grid[self.y][self.x] == 0:
            self.cleanCnt += 1
            self.grid[self.y][self.x] = 2

    def checkLeft(self):
        leftDir = (self.dir + 3) % 4
        leftX = self.x + self.dx[leftDir]
        leftY = self.y + self.dy[leftDir]
        if 0 <= leftX < self.M and 0 <= leftY < self.N:
            return self.grid[leftY][leftX]
        return 1

    def checkBack(self):
        d = (self.dir + 2) % 4
        tx = self.x + self.dx[d]
        ty = self.y + self.dy[d]
        if 0 <= tx < self.M and 0 <= ty < self.N:
            return self.grid[ty][tx]
        return 1

    def start(self):
        self.clean()
        self.checkCnt = 0
        while True:
            if self.checkLeft() == 0:
                self.turnleft()
                self.moveFront()
                self.clean()
                self.checkCnt = 0
            else:
                self.turnleft()
                self.checkCnt += 1
                if self.checkCnt == 4:
                    if self.checkBack() != 1:
                        self.moveBack()
                        self.clean()
                        self.checkCnt = 0
                    else:
                        return


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    robot = Robot(c, r, d, grid, N, M)
    robot.start()
    print(robot.cleanCnt)
    return


if __name__ == "__main__":
    solve()


# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 1 1 1 1 0 1
# 1 0 0 1 1 2 2 2 2 1
# 1 0 1 1 2 2 2 2 2 1
# 1 0 0 0 2 2 2 2 2 1
# 1 0 0 0 2 2 2 1 2 1
# 1 0 0 0 2 2 1 1 2 1
# 1 0 0 0 2 2 1 1 2 1
# 1 0 0 0 2 2 2 2 2 1
# 1 1 1 1 1 1 1 1 1 1
