# https://www.acmicpc.net/problem/1182


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
    N, S = map(int, input().split())
    Nums = merge_sort(list(map(int, input().split())))
    resCnt = 0
    for mask in range(1, 1 << N):
        TempSum = 0
        i = 0
        while i < N:
            if ((1 << i) & mask) > 0:
                TempSum += Nums[i]
            i += 1
        if TempSum == S:
            resCnt += 1
            # if TempSum > S:
            #     break
    print(resCnt)
    return


if __name__ == "__main__":
    solve()
