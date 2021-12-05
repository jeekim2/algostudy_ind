# https://www.acmicpc.net/problem/1920

import sys


def bs(target, left, right):
    global references

    mid = (left + right) // 2
    if target == references[mid]:
        return 1
    if left >= right:
        return 0
    if target > references[mid]:
        return bs(target, mid + 1, right)
    return bs(target, left, mid - 1)


def solve():
    input = sys.stdin.readline
    global references
    N = int(input())
    references = list(map(int, input().split()))
    M = int(input())
    targets = list(map(int, input().split()))

    references.sort()  # Binary search 를 사용하기 위해 reference를 ascending 정렬

    for target in targets:
        print(bs(target, 0, N - 1))


if __name__ == "__main__":
    solve()
