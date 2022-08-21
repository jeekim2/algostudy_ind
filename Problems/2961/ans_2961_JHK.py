# https://www.acmicpc.net/problem/2961

import sys


def get_sour_bitter_diff(sel, Ingred, N):
    i = 0
    sour = 1
    bitter = 0
    while i < N:
        if 1 << i & sel > 0:
            sour *= Ingred[i][0]
            bitter += Ingred[i][1]
        i += 1
    return abs(sour - bitter)


def solve():
    input = sys.stdin.readline
    N = int(input())
    Ingred = [tuple(map(int, input().split())) for _ in range(N)]
    MinDiff = 1000000000
    for sel in range(1, 1 << N):
        MinDiff = min(MinDiff, get_sour_bitter_diff(sel, Ingred, N))
    print(MinDiff)
    return


if __name__ == "__main__":
    solve()
