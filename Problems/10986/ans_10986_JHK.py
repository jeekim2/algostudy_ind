# https://www.acmicpc.net/problem/10986


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
    N, M = map(int, input().split())
    Nums = list(map(int, input().split()))
    PSum = [0]
    Temp = 0
    for num in Nums:
        Temp = (Temp + num) % M
        PSum.append(Temp)
    PSum = merge_sort(PSum)
    BeforeVal = 0
    cnt = 0
    res = [1] * M
    for v in PSum:
        if BeforeVal != v:
            res[BeforeVal] = cnt
            cnt = 1
            BeforeVal = v
        else:
            cnt += 1
    res[BeforeVal] = cnt
    resCnt = 0
    for v in res:
        resCnt += (v - 1) * v // 2
    print(resCnt)
    return


if __name__ == "__main__":
    solve()
