# https://www.acmicpc.net/problem/16938


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
    N, L, R, X = map(int, input().split())
    Nums = merge_sort(list(map(int, input().split())))
    cnt = 0
    for i in range(1 << N):
        j = 0
        ProbSum = 0
        MinProb = 0
        MaxProb = 0
        while j < N:
            if i & (1 << j) > 0:
                ProbSum += Nums[j]
                if MinProb == 0:
                    MinProb = Nums[j]
                MaxProb = Nums[j]
            j += 1
        if L > ProbSum or ProbSum > R:
            continue
        if MinProb != 0 and MaxProb != 0 and MaxProb - MinProb >= X:
            cnt += 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
