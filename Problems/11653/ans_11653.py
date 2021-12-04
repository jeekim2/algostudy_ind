# https://www.acmicpc.net/problem/11653

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    div = 2
    while N != 1:
        if N % div == 0:
            print(div)
            N /= div
        else:
            div += 1
    return


if __name__ == "__main__":
    solve()
