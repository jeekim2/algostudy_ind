# https://www.acmicpc.net/problem/4948

import sys


def solve():
    input = sys.stdin.readline
    inputList = []
    while True:
        N = int(input())
        if N == 0:
            break
        inputList.append(N)

    res = [True] * (max(inputList) * 2 + 1)

    for inp in range(2, max(inputList) * 2 + 1):
        if res[inp]:
            i = 2
            while inp * i < max(inputList) * 2 + 1:
                res[inp * i] = False
                i += 1

    for inp in inputList:
        cnt = 0
        for i in range(inp + 1, inp * 2 + 1):
            if res[i]:
                cnt += 1
        print(cnt)

    return


if __name__ == "__main__":
    solve()
