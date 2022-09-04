# https://www.acmicpc.net/problem/16507

import sys


def sum_partial_pic(PicSum, r1, c1, r2, c2):
    res = 0
    for r in range(r1, r2 + 1):
        res += PicSum[r][c2 + 1] - PicSum[r][c1]
    res //= (r2 - r1 + 1) * (c2 - c1 + 1)
    return res


def solve():
    input = sys.stdin.readline
    R, C, Q = map(int, input().split())
    PicSum = []
    for _ in range(R):
        TempSum = [0]
        Temp = 0
        Pic = list(map(int, input().split()))
        for p in Pic:
            Temp += p
            TempSum.append(Temp)
        PicSum.append(TempSum)

    TC = []
    for _ in range(Q):
        r1, c1, r2, c2 = map(int, input().split())
        TC.append((r1 - 1, c1 - 1, r2 - 1, c2 - 1))
    for t in TC:
        print(sum_partial_pic(PicSum, *t))
    return


if __name__ == "__main__":
    solve()
