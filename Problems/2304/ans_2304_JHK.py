# https://www.acmicpc.net/problem/2304

import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
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
    Polls = []
    MaxHeight = 0
    for _ in range(N):
        i, h = map(int, input().split())
        MaxHeight = max(MaxHeight, h)
        Polls.append((i, h))
    Polls = merge_sort(Polls)
    leftstack = []
    rightstack = []
    OldHeight = 0
    for i, h in Polls:
        if h > OldHeight:
            leftstack.append((i, h))
            OldHeight = h
        if h >= MaxHeight:
            break

    OldHeight = 0
    for i, h in Polls[::-1]:
        if h > OldHeight:
            rightstack.append((i, h))
            OldHeight = h
        if h >= MaxHeight:
            break
    res = (rightstack[-1][0] - leftstack[-1][0] + 1) * rightstack[-1][1]
    for i in range(len(leftstack) - 1):
        res += (leftstack[i + 1][0] - leftstack[i][0]) * leftstack[i][1]
    for i in range(len(rightstack) - 1):
        res += (rightstack[i][0] - rightstack[i + 1][0]) * rightstack[i][1]
    print(res)
    return


if __name__ == "__main__":
    solve()
