# https://www.acmicpc.net/problem/15724

import sys


def get_pos(x):
    return int(x) - 1


def count_people(PSum, M, y1, x1, y2, x2):
    res = 0
    for y in range(y1, y2 + 1):
        res += PSum[y * M + x2 + 1] - PSum[y * M + x1]
    return res


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    People = []
    for _ in range(N):
        People += list(map(int, input().split()))
    PSum = [0]
    TempSum = 0
    for p in People:
        TempSum += p
        PSum.append(TempSum)
    TC = []
    K = int(input())
    for _ in range(K):
        TC.append(tuple(map(get_pos, input().split())))
    for T in TC:
        print(count_people(PSum, M, *T))
    return


if __name__ == "__main__":
    solve()
