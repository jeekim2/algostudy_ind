# https://www.acmicpc.net/problem/11663

import sys


def bs_left_bound(arr, thd):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] < thd:
            left = mid
        else:
            right = mid

    return right


def bs_right_bound(arr, thd):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] > thd:
            right = mid
        else:
            left = mid
    return left


def count_on_line(Point, l, r):
    return bs_right_bound(Point, r) - bs_left_bound(Point, l) + 1


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
    Point = merge_sort(list(map(int, input().split())))
    Lines = [tuple(map(int, input().split())) for _ in range(M)]
    for l, r in Lines:
        print(count_on_line(Point, l, r))
    return


if __name__ == "__main__":
    solve()
