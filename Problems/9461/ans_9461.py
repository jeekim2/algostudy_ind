# https://www.acmicpc.net/problem/9461

import sys


def padovan(i):
    # P(n) = P(n-1) + P(n-5) in n >= 6
    global memo
    if memo.get(i):
        return memo[i]
    memo[i] = padovan(i - 1) + padovan(i - 5)
    return memo[i]


def solve():
    input = sys.stdin.readline
    global memo
    T = int(input())
    N = []
    memo = {}
    for _ in range(T):
        N.append(int(input()))
    memo[1] = 1
    memo[2] = 1
    memo[3] = 1
    memo[4] = 2
    memo[5] = 2

    for a in N:
        print(padovan(a))
    return


if __name__ == "__main__":
    solve()
