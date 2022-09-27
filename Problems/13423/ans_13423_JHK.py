# https://www.acmicpc.net/problem/13423

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


def cnt_val(arr, val):
    if arr[0] == val:
        leftbound = 0
    else:
        left = 0
        right = len(arr)
        while right - left > 1:
            mid = (left + right) // 2
            if arr[mid] >= val:
                right = mid
            else:
                left = mid
        leftbound = right
    if arr[len(arr) - 1] == val:
        rightbound = len(arr) - 1
    else:
        left = 0
        right = len(arr)
        while right - left > 1:
            mid = (left + right) // 2
            if arr[mid] > val:
                right = mid
            else:
                left = mid
        rightbound = left
    if leftbound == rightbound and arr[leftbound] != val:
        return 0
    return rightbound - leftbound + 1


def count_tri(arr):
    cnt = 0
    i = 0
    while i < len(arr) - 2:
        j = len(arr) - 1
        while j > i + 1:
            if (arr[j] - arr[i]) % 2 == 0:
                cnt += cnt_val(arr[i + 1 : j], arr[i] + (arr[j] - arr[i]) // 2)
            j -= 1
        i += 1
    return cnt


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = []
    for _ in range(T):
        input()
        TC.append(merge_sort(list(map(int, input().split()))))
    for arr in TC:
        print(count_tri(arr))
    return


if __name__ == "__main__":
    solve()
