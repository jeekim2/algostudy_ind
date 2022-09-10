# https://www.acmicpc.net/problem/1049

import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    MinSix = 1001
    MinOne = 1001
    for _ in range(M):
        TempSix, TempOne = map(int, input().split())
        MinSix = min(MinSix, TempSix)
        MinOne = min(MinOne, TempOne)
    if MinOne * 6 <= MinSix:
        print(MinOne * N)
        return
    res = 0
    while N > 0:
        if MinOne * N <= MinSix:
            print(res + MinOne * N)
            return
        N -= 6
        res += MinSix
    print(res)
    return


if __name__ == "__main__":
    solve()
