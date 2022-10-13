# https://www.acmicpc.net/problem/1244

import sys


class Human:
    def __init__(self, start):
        self.startIdx = start

    def turnLight(self):
        return


class Man(Human):
    def turnLight(self, Light: list):
        i = 1
        while i * self.startIdx <= len(Light):
            Light[i * self.startIdx - 1] ^= 1
            i += 1
        return


class Woman(Human):
    def turnLight(self, Light: list):
        i = 1
        Light[self.startIdx - 1] ^= 1
        while self.startIdx - i > 0 and self.startIdx + i <= len(Light):
            if Light[self.startIdx - i - 1] != Light[self.startIdx + i - 1]:
                break
            Light[self.startIdx - i - 1] ^= 1
            Light[self.startIdx + i - 1] ^= 1
            i += 1

        return


def solve():
    input = sys.stdin.readline
    N = int(input())
    Light = list(map(int, input().split()))
    M = int(input())
    S = []
    for _ in range(M):
        S.append(tuple(map(int, input().split())))
    for sex, idx in S:
        if sex == 1:
            std = Man(idx)
        else:
            std = Woman(idx)
        std.turnLight(Light)

    for i in range(len(Light)):
        if i % 20 == 0 and i != 0:
            print()
        print(Light[i], end=" ")
    print()
    return


if __name__ == "__main__":
    solve()
