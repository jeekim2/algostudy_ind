# https://www.acmicpc.net/problem/2231

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())

    digit = len(str(N))

    startNum = N - (digit * 9)
    if startNum < 0:
        startNum = 0

    for i in range(startNum, N):
        temp_sum = i + sum([int(s) for s in str(i)])
        if temp_sum == N:
            print(i)
            return
            # break
    print(0)
    return


if __name__ == "__main__":
    solve()
