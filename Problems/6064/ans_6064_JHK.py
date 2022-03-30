# https://www.acmicpc.net/problem/6064

import sys


def get_year(M, N, x, y):
    if M > N:
        M, N = N, M
        x, y = y, x
    i = 0
    KaIn_valid = False
    while i < M:
        temp = i * N + y - x
        if temp % M == 0:
            KaIn_valid = True
            break
        i += 1
    if KaIn_valid:
        return i * N + y

    return -1


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = []
    for _ in range(T):
        TC.append(list(map(int, input().split())))
    for t in TC:
        print(get_year(*t))
    return


if __name__ == "__main__":
    solve()
