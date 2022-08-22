# https://www.acmicpc.net/problem/17609

import sys


def check_palind(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False, i
    return True, 0


def check_string(s):
    res, idx = check_palind(s)
    if res:
        return 0
    res2, _ = check_palind(s[idx : len(s) - idx - 1])
    res3, _ = check_palind(s[idx + 1 : len(s) - idx])
    if res2 or res3:
        return 1
    return 2


def solve():
    input = sys.stdin.readline
    N = int(input())
    for _ in range(N):
        print(check_string(input().rstrip()))
    return


if __name__ == "__main__":
    solve()
