# https://www.acmicpc.net/problem/21318

import sys


def get_mistake_cnt(PSum_mistake, x, y):

    return PSum_mistake[y - 1] - PSum_mistake[x - 1]


def solve():
    input = sys.stdin.readline
    N = int(input())
    Score = list(map(int, input().split()))
    Mistake = [0] * N
    for i in range(N - 1):
        if Score[i] > Score[i + 1]:
            Mistake[i] = 1
    PSum_mistake = [0]
    TempSum = 0
    for v in Mistake:
        TempSum += v
        PSum_mistake.append(TempSum)

    Q = int(input())
    TC = []
    for _ in range(Q):
        x, y = map(int, input().split())
        TC.append((x, y))
    for x, y in TC:
        print(get_mistake_cnt(PSum_mistake, x, y))
    return


if __name__ == "__main__":
    solve()
