# https://www.acmicpc.net/problem/10211

import sys


def get_max_subarr(arr):
    Prefix_Sum = [0]
    AccSum = 0
    for v in arr:
        AccSum += v
        Prefix_Sum.append(AccSum)
    maxVal = -1001
    for i in range(len(Prefix_Sum)):
        for j in range(i):
            tempval = Prefix_Sum[i] - Prefix_Sum[j]
            if tempval > maxVal:
                maxVal = tempval

    return maxVal


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = []
    for _ in range(T):
        N = int(input())
        TC.append(list(map(int, input().split())))

    for arr in TC:
        print(get_max_subarr(arr))
    return


if __name__ == "__main__":
    solve()
