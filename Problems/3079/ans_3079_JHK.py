# https://www.acmicpc.net/problem/3079

import sys


def CheckIn_Available(Checkpoint, M, TimeLimit):
    cnt = 0
    for c in Checkpoint:
        cnt += TimeLimit // c
    if cnt >= M:
        return True
    return False


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Checkpoint = [int(input()) for _ in range(N)]
    MinTime = 0
    MaxTime = 1
    while True:
        if CheckIn_Available(Checkpoint, M, MaxTime):
            break
        else:
            MinTime = MaxTime
            MaxTime *= 2
    while MaxTime - MinTime > 1:
        t = (MinTime + MaxTime) // 2
        if CheckIn_Available(Checkpoint, M, t):
            MaxTime = t
        else:
            MinTime = t
    print(MaxTime)
    return


if __name__ == "__main__":
    solve()
