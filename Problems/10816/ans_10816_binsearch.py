# https://www.acmicpc.net/problem/10816

import sys


def bs_left(i, left, right):
    global source
    global N
    while True:
        if left == N - 1:
            return -1
        mid = (left + right) // 2
        if left + 1 >= right:
            if source[mid] == i:
                return mid
            if source[mid + 1] == i:
                return mid + 1
            return -1
        if source[mid] >= i:
            right = mid
        else:
            left = mid


def bs_right(i, left, right):
    global source
    global N
    while True:
        mid = (left + right) // 2
        if left + 1 >= right:
            if source[mid] == i:
                return mid
            return -1
        if source[mid] > i:
            right = mid
        else:
            left = mid


def binarysearch(i):
    global source
    global N
    left = 0
    right = N
    while True:
        mid = (left + right) // 2
        if source[mid] == i:
            break
        if left + 1 >= right:
            return 0
        if source[mid] > i:
            right = mid
        else:
            left = mid

    left_end = bs_left(i, left, right)
    if left_end == -1:
        return 0
    right_end = bs_right(i, left_end, right)
    return right_end - left_end + 1


def solve():
    global source
    global N
    input = sys.stdin.readline
    N = int(input())
    source = list(map(int, input().split()))
    M = int(input())
    checks = list(map(int, input().split()))
    source.sort()

    for i in checks:
        print(binarysearch(i), end=" ")
    print()


if __name__ == "__main__":
    solve()
