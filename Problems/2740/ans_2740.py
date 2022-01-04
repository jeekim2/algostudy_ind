# https://www.acmicpc.net/problem/2740

import sys


def solve():
    input = sys.stdin.readline
    # Result dimension : N, K
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    M, K = map(int, input().split())
    B = []
    for _ in range(M):
        B.append(list(map(int, input().split())))

    # Transpose B
    Bt = list(map(list, zip(*B)))

    res = []
    resIdx = 0
    for rowA in A:
        res.append([])
        for rowB in Bt:
            elementSum = 0
            for i in range(M):
                elementSum += rowA[i] * rowB[i]
            res[-1].append(elementSum)
        # resIdx += 1
        # if resIdx == M:

    for r in res:
        for x in r:
            print(x, end=" ")
        print()
    return


if __name__ == "__main__":
    solve()
