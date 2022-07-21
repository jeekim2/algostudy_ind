# https://www.acmicpc.net/problem/3649

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


def search_match_block(target, base, Blocks):
    target -= Blocks[base]
    left = base + 1
    right = len(Blocks)
    while right - left > 0:
        mid = (left + right) // 2
        if target == Blocks[mid]:
            return True, mid
        if target < Blocks[mid]:
            right = mid
        else:
            left = mid + 1
    return False, None


def search_two_blocks(x, Blocks):
    Blocks = merge_sort(Blocks)
    i = 0
    while i < len(Blocks) - 1:
        res, val = search_match_block(x, i, Blocks)
        if res:
            print(f"yes {Blocks[i]} {Blocks[val]}")
            return
        i += 1
    print("danger")
    return


def solve():
    input = sys.stdin.readline
    while True:
        try:
            x = int(input()) * 10000000
            N = int(input())
            Blocks = []
            for j in range(N):
                b = int(input())
                if b < x:
                    Blocks.append(b)
            search_two_blocks(x, Blocks)
        except:
            break
    return


if __name__ == "__main__":
    solve()
