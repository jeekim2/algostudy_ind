# https://www.acmicpc.net/problem/10816

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    source = list(map(int, input().split()))
    M = int(input())
    checks = list(map(int, input().split()))

    dict = {}
    for i in source:
        if dict.get(i) == None:
            dict[i] = 1
        else:
            dict[i] += 1

    for i in checks:
        if dict.get(i) == None:
            print(0, end=" ")
        else:
            print(dict[i], end=" ")
    print()


if __name__ == "__main__":
    solve()
