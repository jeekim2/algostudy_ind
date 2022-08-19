# https://www.acmicpc.net/problem/2531

import sys


def solve():
    input = sys.stdin.readline
    N, d, k, c = map(int, input().split())
    c -= 1
    Chobap = []
    for _ in range(N):
        Chobap.append(int(input()) - 1)
    ChobapCnt = [0] * d
    for i in range(k):
        ChobapCnt[Chobap[i]] += 1
    ChobapCntRes = 0
    for v in ChobapCnt:
        if v:
            ChobapCntRes += 1
    i = 0
    maxCnt = 0
    while i < N:
        ChobapCnt[Chobap[i]] -= 1
        if ChobapCnt[Chobap[i]] == 0:
            ChobapCntRes -= 1
        if i + k >= N:
            p = i + k - N
        else:
            p = i + k
        if ChobapCnt[Chobap[p]] == 0:
            ChobapCntRes += 1
        ChobapCnt[Chobap[p]] += 1
        i += 1
        if ChobapCnt[c] == 0:
            maxCnt = max(maxCnt, ChobapCntRes + 1)
        else:
            maxCnt = max(maxCnt, ChobapCntRes)
    print(maxCnt)
    return


if __name__ == "__main__":
    solve()
