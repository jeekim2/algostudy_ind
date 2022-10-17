# https://www.acmicpc.net/problem/14891

import sys


class Gear:
    def __init__(self, teeth, score):
        self.teeth = teeth
        self.score = score
        self.left = 6
        self.right = 2
        self.top = 0
        self.next = None
        self.prev = None

    def link_next(self, nextGear):
        self.next = nextGear
        nextGear.prev = self

    def get_score(self):
        return self.score * int(self.teeth[self.top])

    def turn_CCW(self):
        self.top += 1
        self.top %= 8
        self.left += 1
        self.left %= 8
        self.right += 1
        self.right %= 8

    def turn_CW(self):
        self.top -= 1
        if self.top < 0:
            self.top += 8
        self.left -= 1
        if self.left < 0:
            self.left += 8
        self.right -= 1
        if self.right < 0:
            self.right += 8

    def turn(self, direction):
        if direction == 1:
            # CW
            self.turn_CW()
        else:
            # CCW
            self.turn_CCW()

    def check_next_avail(self):
        if self.next is not None:
            if self.next.teeth[self.next.left] != self.teeth[self.right]:
                return True
        return False

    def check_prev_avail(self):
        if self.prev is not None:
            if self.prev.teeth[self.prev.right] != self.teeth[self.left]:
                return True
        return False

    def turn_start(self, direction):
        if self.check_next_avail():
            self.next.turn_from_prev(direction * (-1))
        if self.check_prev_avail():
            self.prev.turn_from_next(direction * (-1))
        self.turn(direction)

    def turn_from_prev(self, direction):
        if self.check_next_avail():
            self.next.turn_from_prev(direction * (-1))
        self.turn(direction)

    def turn_from_next(self, direction):
        if self.check_prev_avail():
            self.prev.turn_from_next(direction * (-1))
        self.turn(direction)


def solve():
    input = sys.stdin.readline
    Gears = [Gear(input().rstrip(), 2**i) for i in range(4)]
    K = int(input())
    cmd = [tuple(map(int, input().split())) for _ in range(K)]
    for i in range(3):
        Gears[i].link_next(Gears[i + 1])
    for i, d in cmd:
        Gears[i - 1].turn_start(d)
    res = 0
    for i in range(4):
        res += Gears[i].get_score()
    print(res)
    return


if __name__ == "__main__":
    solve()
