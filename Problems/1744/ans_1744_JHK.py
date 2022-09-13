# https://www.acmicpc.net/problem/1744

import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        return res

    return merge(merge_sort(arr[: len(arr) // 2]), merge_sort(arr[len(arr) // 2 :]))


def solve():
    input = sys.stdin.readline
    N = int(input())
    NegNums = []
    PosNums = []
    Zeros = []
    Ones = []
    for _ in range(N):
        v = int(input())
        if v == 1:
            Ones.append(v)
        elif v > 0:
            PosNums.append(v)
        elif v < 0:
            NegNums.append(v)
        else:
            Zeros.append(v)
    PosNums = merge_sort(PosNums)
    NegNums = merge_sort(NegNums)
    res = sum(Ones)
    if len(PosNums) % 2 == 0:
        i = 0
        while i < len(PosNums) - 1:
            res += PosNums[i] * PosNums[i + 1]
            i += 2
    else:
        res += PosNums[0]
        i = 1
        while i < len(PosNums) - 1:
            res += PosNums[i] * PosNums[i + 1]
            i += 2
    i = 0
    while i < len(NegNums) - 1:
        res += NegNums[i] * NegNums[i + 1]
        i += 2
    if len(NegNums) % 2 == 0:
        print(res)
    else:
        if len(Zeros) > 0:
            print(res)
        else:
            print(res + NegNums[-1])
    return


if __name__ == "__main__":
    solve()
