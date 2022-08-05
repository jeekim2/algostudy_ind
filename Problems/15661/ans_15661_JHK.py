# https://www.acmicpc.net/problem/15661

import sys


def get_score(Status, N, x, y):
    return Status[x * N + y] + Status[y * N + x]


def get_score_diff(Status, N, select):
    res = 0
    for i in range(N):
        if select & 1 << i:
            for j in range(i):
                if select & 1 << j:
                    res += get_score(Status, N, i, j)
    select = select ^ ((1 << N) - 1)
    res2 = 0
    for i in range(N):
        if select & 1 << i:
            for j in range(i):
                if select & 1 << j:
                    res2 += get_score(Status, N, i, j)
    return abs(res - res2)


def solve():
    input = sys.stdin.readline
    N = int(input())
    Status = []
    for _ in range(N):
        Status += list(map(int, input().split()))
    minDiff = N * (N - 1) * 50 + 1
    for sel in range(1, 1 << N):
        if sel <= sel ^ ((1 << N) - 1):
            minDiff = min(minDiff, get_score_diff(Status, N, sel))
    print(minDiff)
    return


if __name__ == "__main__":
    solve()
