# https://www.acmicpc.net/problem/2564

import sys


def get_relative_position(XDir, XPos, W, H):
    if XDir == 1:
        return H + XPos
    if XDir == 2:
        return H + H + W + W - XPos
    if XDir == 3:
        return H - XPos
    return H + W + XPos


def solve():
    input = sys.stdin.readline
    W, H = map(int, input().split())
    Around = 2 * (H + W)
    N = int(input())
    Stores = []
    for _ in range(N):
        Stores.append(get_relative_position(*tuple(map(int, input().split())), W, H))
    X = get_relative_position(*tuple(map(int, input().split())), W, H)
    Dist = 0
    for s in Stores:
        Dist += min(abs(X - s), Around - abs(X - s))
    print(Dist)
    return


if __name__ == "__main__":
    solve()
