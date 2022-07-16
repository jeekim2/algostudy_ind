# https://www.acmicpc.net/problem/5567

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    Friends = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        Friends[A - 1].append(B - 1)
        Friends[B - 1].append(A - 1)
    InviteList = set()
    for f in Friends[0]:
        InviteList.add(f)
        for ff in Friends[f]:
            InviteList.add(ff)
    InviteList.discard(0)
    print(len(InviteList))
    return


if __name__ == "__main__":
    solve()
