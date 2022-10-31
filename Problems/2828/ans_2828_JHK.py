# https://www.acmicpc.net/problem/2828

import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    J = int(input())
    Pos = []
    for _ in range(J):
        Pos.append(int(input()))
    BoxPos = 1
    cnt = 0
    for p in Pos:
        if BoxPos <= p <= BoxPos + M - 1:
            continue
        elif p < BoxPos:
            cnt += BoxPos - p
            BoxPos = p
        else:
            cnt += p - (BoxPos + M - 1)
            BoxPos = p - (M - 1)
    print(cnt)
    return


if __name__ == "__main__":
    solve()
