# https://www.acmicpc.net/problem/1802

import sys


def checkPattern(s):
    if len(s) == 1:
        return True
    mid = len(s) // 2
    for i in range(1, len(s) - mid):
        if s[mid + i] == s[mid - i]:
            return False
    return checkPattern(s[:mid])


def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = [input().rstrip() for _ in range(N)]
    for s in TC:
        if checkPattern(s):
            print("YES")
        else:
            print("NO")
    return


if __name__ == "__main__":
    solve()
