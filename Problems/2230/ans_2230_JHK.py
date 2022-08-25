# https://www.acmicpc.net/problem/2230

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
    N, M = map(int, input().split())
    Nums = merge_sort([int(input()) for _ in range(N)])
    if M == 0:
        print(0)
        return
    i = 0
    j = 1
    MinDiff = 2000000001
    while j < N:
        TempRes = Nums[j] - Nums[i]
        if TempRes == M:
            print(M)
            return
        if TempRes > M:
            i += 1
            if TempRes < MinDiff:
                MinDiff = TempRes
        else:
            j += 1

    print(MinDiff)
    return


if __name__ == "__main__":
    solve()
