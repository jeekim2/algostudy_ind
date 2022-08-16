# https://www.acmicpc.net/problem/3020

import sys


def get_cnt(v, H, SctiteSum, SgmiteSum):
    return SctiteSum[-1] - SctiteSum[v - 1] + SgmiteSum[-1] - SgmiteSum[H - v]


def solve():
    input = sys.stdin.readline
    N, H = map(int, input().split())
    Stalactite = [0] * (H + 1)
    Stalagmite = [0] * (H + 1)
    for i in range(N):
        B = int(input())
        if i % 2 == 0:
            # 종유석
            Stalactite[B] += 1
        else:
            # 석순
            Stalagmite[B] += 1
    SctiteSum = []
    SgmiteSum = []
    Temp = 0
    for v in Stalactite:
        Temp += v
        SctiteSum.append(Temp)
    Temp = 0
    for v in Stalagmite:
        Temp += v
        SgmiteSum.append(Temp)
    res = [0] * (N + 1)
    for i in range(1, H + 1):
        res[get_cnt(i, H, SctiteSum, SgmiteSum)] += 1
    for i, r in enumerate(res):
        if r != 0:
            print(i, r)
            return
    return


if __name__ == "__main__":
    solve()
