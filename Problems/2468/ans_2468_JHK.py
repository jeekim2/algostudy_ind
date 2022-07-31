# https://www.acmicpc.net/problem/2468

import sys

sys.setrecursionlimit(10001)


def setDryGround(H, Ground, isDryGround):
    for i, level in enumerate(Ground):
        if level > H:
            isDryGround[i] = True
    return


def visit_Island(N, isDryGround, i):
    if isDryGround[i]:
        x, y = i % N, i // N
        isDryGround[i] = False
        if x > 0:
            visit_Island(N, isDryGround, y * N + x - 1)
        if x < N - 1:
            visit_Island(N, isDryGround, y * N + x + 1)
        if y > 0:
            visit_Island(N, isDryGround, (y - 1) * N + x)
        if y < N - 1:
            visit_Island(N, isDryGround, (y + 1) * N + x)
        return


def countIsland(N, isDryGround):
    cnt = 0
    for i, v in enumerate(isDryGround):
        if v:
            visit_Island(N, isDryGround, i)
            cnt += 1
    return cnt


def solve():
    input = sys.stdin.readline
    N = int(input())
    Ground = []
    for _ in range(N):
        Ground += list(map(int, input().split()))
    isDryGround = [False] * len(Ground)
    MaxHeight = max(Ground)
    cnt = 1
    for H in range(min(Ground), max(Ground)):
        setDryGround(H, Ground, isDryGround)
        cnt = max(cnt, countIsland(N, isDryGround))
    print(cnt)
    return


if __name__ == "__main__":
    solve()
