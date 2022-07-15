# https://www.acmicpc.net/problem/11501

import sys


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = []
    for _ in range(T):
        N = int(input())
        TC.append(list(map(int, input().split())))
    for prices in TC:
        currentMax = 0
        gain = 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] < currentMax:
                gain += currentMax - prices[i]
            else:
                currentMax = prices[i]
        print(gain)
    return


if __name__ == "__main__":
    solve()
