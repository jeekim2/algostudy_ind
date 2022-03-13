# https://www.acmicpc.net/problem/11576

import sys


def TransAtoB(NumA, A, B):
    NumA.reverse()
    pow = 0
    res = 0
    for n in NumA:
        res += (A ** pow) * n
        pow += 1

    NumB = []
    pow = 0
    tempB = 1
    while tempB < res:
        tempB *= B
        pow += 1

    tempB = tempB // B
    pow -= 1
    while pow >= 0:

        NumB.append(res // tempB)
        res %= tempB
        tempB = tempB // B
        pow -= 1

    return NumB


def solve():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    m = int(input())
    NumberA = list(map(int, input().split()))
    print(*TransAtoB(NumberA, A, B))
    return


if __name__ == "__main__":
    solve()
