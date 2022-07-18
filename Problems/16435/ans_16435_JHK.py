# https://www.acmicpc.net/problem/16435


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
    Trees = merge_sort(list(map(int, input().split())))
    for t in Trees:
        if t <= L:
            L += 1
        else:
            break
    print(L)
    return


if __name__ == "__main__":
    solve()
