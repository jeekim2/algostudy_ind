# https://www.acmicpc.net/problem/1339

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
    Words = []
    Score = [0] * 26
    for _ in range(N):
        s = input().rstrip()
        lv = 1
        for c in s[::-1]:
            cIdx = ord(c) - ord("A")
            Score[cIdx] += lv
            lv *= 10
    rankScore = merge_sort(Score)
    s = 9
    res = 0
    for v in rankScore:
        if v == 0:
            break
        res += s * v
        s -= 1
    print(res)
    return


if __name__ == "__main__":
    solve()
