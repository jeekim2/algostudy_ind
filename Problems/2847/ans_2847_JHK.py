# https://www.acmicpc.net/problem/2847
import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    Levels = [int(input()) for _ in range(N)]
    cnt = 0
    for i in range(N - 2, -1, -1):
        while Levels[i] >= Levels[i + 1]:
            cnt += 1
            Levels[i] -= 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
