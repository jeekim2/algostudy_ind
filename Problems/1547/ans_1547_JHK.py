# https://www.acmicpc.net/problem/1547
import sys


def solve():
    input = sys.stdin.readline
    M = int(input())
    cmd = [tuple(map(int, input().split())) for _ in range(M)]
    Cups = [1, 2, 3]
    for x, y in cmd:
        Cups[x - 1], Cups[y - 1] = Cups[y - 1], Cups[x - 1]
    for i, c in enumerate(Cups):
        if c == 1:
            print(i + 1)
    return


if __name__ == "__main__":
    solve()
