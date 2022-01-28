# https://www.acmicpc.net/problem/1520

# 시간초과 - 단순 재귀 (from 0,0)

import sys


def getPathNum(data, pathNum, rowi, colj):
    if pathNum[rowi][colj] != None:
        return pathNum[rowi][colj]

    ref = data[rowi][colj]
    res = 0
    if rowi > 0:
        if ref < data[rowi - 1][colj]:
            # UP
            res += getPathNum(data, pathNum, rowi - 1, colj)
    if rowi < N - 1:
        if ref < data[rowi + 1][colj]:
            # DOWN
            res += getPathNum(data, pathNum, rowi + 1, colj)
    if colj > 0:
        if ref < data[rowi][colj - 1]:
            # LEFT
            res += getPathNum(data, pathNum, rowi, colj - 1)
    if colj < M - 1:
        if ref < data[rowi][colj + 1]:
            # RIGHT
            res += getPathNum(data, pathNum, rowi, colj + 1)
    pathNum[rowi][colj] = res
    return res


# 일반 재귀로는 여기까지
# def getPathNum(data, rowi, colj):
#     ref = data[rowi][colj]
#     if rowi == 0 and colj == 0:
#         res = 1
#     else:
#         res = 0
#     if rowi > 0:
#         if ref < data[rowi - 1][colj]:
#             # UP
#             res += getPathNum(data, rowi - 1, colj)
#     if rowi < N - 1:
#         if ref < data[rowi + 1][colj]:
#             # DOWN
#             res += getPathNum(data, rowi + 1, colj)
#     if colj > 0:
#         if ref < data[rowi][colj - 1]:
#             # LEFT
#             res += getPathNum(data, rowi, colj - 1)
#     if colj < M - 1:
#         if ref < data[rowi][colj + 1]:
#             # RIGHT
#             res += getPathNum(data, rowi, colj + 1)
#     return res


def solve():
    global N, M
    input = sys.stdin.readline
    N, M = map(int, input().split())
    pathNum = [[None] * M for _ in range(N)]
    res = [[0] * M for _ in range(N)]
    data = []
    for _ in range(N):
        data.append(tuple(map(int, input().split())))
    pathNum[0][0] = 1

    """
    res = getPathNum(data, N - 1, M - 1)
    # 그냥 재귀 돌릴 경우
    """

    # 적당히 재귀 횟수를 줄일 수 있을만큼만 Bottom-up
    for i in range(min(N, M)):
        for j in range(i + 1):
            getPathNum(data, pathNum, j, i - j)

    # 최종 결과는 Top-down으로 재귀로 계산
    res = getPathNum(data, pathNum, N - 1, M - 1)

    print(res)
    return


if __name__ == "__main__":
    solve()
