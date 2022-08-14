# https://www.acmicpc.net/problem/11656


def diff_postfix(left, right):
    i = 0
    while True:
        if i >= len(right):
            return False
        if i >= len(left):
            return True
        if left[i] == right[i]:
            i += 1
            continue
        if left[i] < right[i]:
            return True
        else:
            return False


def PostFixSort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            tempRes = diff_postfix(left[i], right[j])
            if tempRes:
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

    return merge(PostFixSort(arr[: len(arr) // 2]), PostFixSort(arr[len(arr) // 2 :]))


def solve():
    s = input()
    PostFixList = []
    for i in range(len(s)):
        PostFixList.append(s[i:])
    Res = PostFixSort(PostFixList)
    for r in Res:
        print(r)
    return


if __name__ == "__main__":
    solve()
