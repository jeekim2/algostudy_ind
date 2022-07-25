# https://www.acmicpc.net/problem/2485

import sys


def GCD(P, Q):
    if P < Q:
        P, Q = Q, P
    while Q != 0:
        P, Q = Q, P % Q
    return P


def solve():
    input = sys.stdin.readline
    N = int(input())
    Trees = [int(input()) for _ in range(N)]
    i = 0
    Gaps = []
    while i < len(Trees) - 1:
        Gaps.append(Trees[i + 1] - Trees[i])
        i += 1
    i = 1
    P = Gaps[0]
    while i < len(Gaps):
        Q = Gaps[i]
        P = GCD(P, Q)
        i += 1

    print((max(Trees) - min(Trees)) // P - len(Trees) + 1)
    return


if __name__ == "__main__":
    solve()
