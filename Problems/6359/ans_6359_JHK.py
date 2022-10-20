# https://www.acmicpc.net/problem/6359

import sys


def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())

        Res = [True] * (N + 1)
        Res[0] = False
        for i in range(2, N + 1):
            j = 1
            while i * j <= N:
                Res[i * j] = not Res[i * j]
                j += 1
        print(Res.count(True))
    return


if __name__ == "__main__":
    solve()
