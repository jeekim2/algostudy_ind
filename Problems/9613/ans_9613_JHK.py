# https://www.acmicpc.net/problem/9613

import sys


def GCD(p, q):
    if p < q:
        p, q = q, p
    while q != 0:
        p, q = q, p % q
    return p


def get_GcdSum(NumList):
    res = 0
    for i in range(len(NumList)):
        for j in range(i + 1, len(NumList)):
            res += GCD(NumList[i], NumList[j])
    return res


def solve():
    t = int(input())
    TC = []
    for _ in range(t):
        TC.append(list(map(int, input().split()))[1:])

    for T in TC:
        print(get_GcdSum(T))
    return


if __name__ == "__main__":
    solve()
