# https://www.acmicpc.net/problem/3135

import sys


def solve():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    MinCnt = abs(B - A)
    N = int(input())
    for _ in range(N):
        P = int(input())
        if MinCnt > abs(B - P) + 1:
            MinCnt = abs(B - P) + 1
    print(MinCnt)
    return


if __name__ == "__main__":
    solve()
