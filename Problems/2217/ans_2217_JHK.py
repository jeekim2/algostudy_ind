# https://www.acmicpc.net/problem/2217

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
    Rope = merge_sort([int(input()) for _ in range(N)])
    MaxWeight = 0
    for i in range(N):
        NumRope = N - i
        WeightLimit = Rope[i]
        MaxWeight = max(MaxWeight, WeightLimit * NumRope)
    print(MaxWeight)
    return


if __name__ == "__main__":
    solve()
