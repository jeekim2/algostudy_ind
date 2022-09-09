# https://www.acmicpc.net/problem/1946

import sys


def sort_score(Score):
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

    TempScore = merge_sort(Score)
    res = []
    for s1, s2 in TempScore:
        res.append(s2)
    return res


def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        Score = [tuple(map(int, input().split())) for _ in range(N)]
        SortedScore = sort_score(Score)
        MinScore = 100001
        cnt = 0
        for s in SortedScore:
            if MinScore > s:
                cnt += 1
                MinScore = s
                if MinScore == 1:
                    break
        print(cnt)
    return


if __name__ == "__main__":
    solve()


# 1 4 - O
# 2 5 - X
# 3 6 - X
# 4 2 - O
# 5 7 - X
# 6 1 - O
# 7 3 - X
