# https://www.acmicpc.net/problem/17425

import sys


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = [int(input()) for _ in range(T)]
    MaxNum = max(TC)
    Divs = [1] * (MaxNum + 1)
    Divs[0] = 0
    for d in range(2, MaxNum + 1):
        idx = 1
        while d * idx <= MaxNum:
            Divs[d * idx] += d
            idx += 1
    DivSum = []
    Temp = 0
    for d in Divs:
        Temp += d
        DivSum.append(Temp)
    for v in TC:
        print(DivSum[v])
    return


if __name__ == "__main__":
    solve()
