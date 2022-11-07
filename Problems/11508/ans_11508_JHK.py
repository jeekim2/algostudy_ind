# https://www.acmicpc.net/problem/11508

import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
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
    Books = merge_sort([int(input()) for _ in range(N)])
    price = 0
    for i, b in enumerate(Books):
        if i % 3 != 2:
            price += b
    print(price)
    return


if __name__ == "__main__":
    solve()
