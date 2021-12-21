# https://www.acmicpc.net/problem/1002

import sys


def searchTarget(TC):
    x1, y1, r1, x2, y2, r2 = TC

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        return
    # r1 = r1 ** 2
    # r2 = r2 ** 2
    r3 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    rs = sorted([r1, r2, r3])
    if rs[2] > rs[1] + rs[0]:
        print(0)
        return
    if rs[2] == rs[1] + rs[0]:
        print(1)
        return
    print(2)
    return


def solve():
    input = sys.stdin.readline
    T = int(input())
    TCs = []
    for _ in range(T):
        TCs.append(list(map(int, input().split())))

    for TC in TCs:
        searchTarget(TC)

    return


if __name__ == "__main__":
    solve()
