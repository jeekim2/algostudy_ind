# https://www.acmicpc.net/problem/17103

import sys


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = [int(input()) for _ in range(T)]
    PrimeNum = [True] * (max(TC) + 1)
    PrimeNum[0] = False
    PrimeNum[1] = False
    for i in range(2, len(PrimeNum)):
        if PrimeNum[i]:
            for j in range(2 * i, len(PrimeNum), i):
                PrimeNum[j] = False

    for N in TC:
        i = 0
        cnt = 0
        while i <= N // 2:
            if PrimeNum[i] and PrimeNum[N - i]:
                cnt += 1
            i += 1
        print(cnt)
    return


if __name__ == "__main__":
    solve()
