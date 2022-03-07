# https://www.acmicpc.net/problem/19637

import sys


def get_title(Title, Thd, Power):
    left = 0
    right = len(Thd)
    while left < right:
        mid = (left + right) // 2
        if Thd[mid] < Power:
            left = mid + 1
        else:
            right = mid

    return Title[left]


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Title = []
    Thd = []
    res = []
    for _ in range(N):
        TempTitle, TempThd = input().split()
        Title.append(TempTitle)
        Thd.append(int(TempThd))
    for _ in range(M):
        res.append(get_title(Title, Thd, int(input())))

    for r in res:
        print(r)
    return


if __name__ == "__main__":
    solve()
