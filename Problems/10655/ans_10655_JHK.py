# https://www.acmicpc.net/problem/10655

import sys


def get_taxi_dst(CheckPoints, StartIdx, EndIdx):
    x_diff = abs(CheckPoints[StartIdx][0] - CheckPoints[EndIdx][0])
    y_diff = abs(CheckPoints[StartIdx][1] - CheckPoints[EndIdx][1])
    return x_diff + y_diff


def get_diff_taxi_dst(CheckPoints, idx):
    OriginalDst = get_taxi_dst(CheckPoints, idx - 1, idx) + get_taxi_dst(
        CheckPoints, idx, idx + 1
    )
    SkippedDst = get_taxi_dst(CheckPoints, idx - 1, idx + 1)
    return OriginalDst - SkippedDst


def solve():
    input = sys.stdin.readline
    N = int(input())
    CheckPoints = []
    for _ in range(N):
        CheckPoints.append(tuple(map(int, input().split())))

    MaxDstDiff = 0
    for i in range(1, N - 1):
        TempDstDiff = get_diff_taxi_dst(CheckPoints, i)
        if TempDstDiff > MaxDstDiff:
            MaxDstDiff = TempDstDiff

    DstSum = 0
    for i in range(0, N - 1):
        DstSum += get_taxi_dst(CheckPoints, i, i + 1)

    print(DstSum - MaxDstDiff)
    return


if __name__ == "__main__":
    solve()
