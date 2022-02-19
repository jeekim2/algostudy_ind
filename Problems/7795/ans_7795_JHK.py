# https://www.acmicpc.net/problem/7795

import sys


def bs(Target, RefList):
    left = 0
    right = len(RefList)

    while left < right - 1:
        mid = (left + right) // 2
        if RefList[mid] < Target:
            left = mid
        else:
            right = mid
    if left == 0:
        if RefList[left] >= Target:
            # 모두 Target 보다 큰 경우 left == mid == 0으로 수렴
            return 0
    # left는 index 이므로, 갯수는 +1
    return left + 1


def quick_sort(RefList):
    if len(RefList) <= 1:
        return RefList
    pivot = RefList[-1]
    mid = [pivot]
    left = []
    right = []
    for val in RefList[:-1]:
        if val < pivot:
            left.append(val)
        elif val > pivot:
            right.append(val)
        else:
            # val == pivot
            mid.append(val)
    return quick_sort(left) + mid + quick_sort(right)


def solve():
    input = sys.stdin.readline
    TC_NUM = int(input())
    res = []
    for _ in range(TC_NUM):
        A_NUM, B_NUM = map(int, input().split())
        AList = list(map(int, input().split()))
        BList = quick_sort(list(map(int, input().split())))

        tempRes = 0
        for A in AList:
            tempRes += bs(A, BList)
        res.append(tempRes)
    for r in res:
        print(r)
    return


if __name__ == "__main__":
    solve()
