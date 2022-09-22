# https://www.acmicpc.net/problem/14241


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
    res = 0
    Slime = Nums[-1]
    i = len(Nums) - 2
    while i >= 0:
        res += Slime * Nums[i]
        Slime += Nums[i]
        i -= 1
    print(res)
    return


if __name__ == "__main__":
    solve()
