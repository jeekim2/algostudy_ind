# https://www.acmicpc.net/problem/18111

import sys


def get_build_time(Ground, h, B):
    res = 0
    for v in Ground:
        if v > h:
            res += 2 * (v - h)
            B += v - h
        else:
            res += h - v
            B -= h - v
    if B < 0:
        return -1
    return res


def solve():
    input = sys.stdin.readline
    N, M, B = map(int, input().split())
    Ground = [0] * (N * M)
    i = 0
    for _ in range(N):
        for v in list(map(int, input().split())):
            Ground[i] = v
            i += 1
    minTime = 256 * 2 * 500 * 500
    minHeight = 256
    for h in range(min(Ground), max(Ground) + 1):
        t = get_build_time(Ground, h, B)
        if t == -1:
            break
        if minTime >= t:
            minHeight = h
            minTime = t
        else:
            break
    print(minTime, minHeight)
    return


if __name__ == "__main__":
    solve()
