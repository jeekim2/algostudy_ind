# https://www.acmicpc.net/problem/1449


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
    N, L = map(int, input().split())
    Cracks = merge_sort(list(map(int, input().split())))
    cnt = 1
    RemainTape = L
    LastCrack = Cracks[0]
    for crack in Cracks:
        CrackGap = crack - LastCrack
        if RemainTape <= CrackGap:
            cnt += 1
            RemainTape = L
        else:
            RemainTape -= CrackGap
        LastCrack = crack
    print(cnt)
    return


if __name__ == "__main__":
    solve()
