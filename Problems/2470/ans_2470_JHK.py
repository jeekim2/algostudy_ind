# https://www.acmicpc.net/problem/2470


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
    N = int(input())
    Nums = merge_sort(list(map(int, input().split())))
    i = 0
    j = N - 1
    MinSum = 2000000001
    while i < j:
        TempRes = Nums[i] + Nums[j]
        if TempRes == 0:
            print(Nums[i], Nums[j])
            return
        if abs(TempRes) < MinSum:
            MinSum = abs(TempRes)
            res = [Nums[i], Nums[j]]
        if TempRes < 0:
            i += 1
        else:
            j -= 1
    print(*res)
    return


if __name__ == "__main__":
    solve()
