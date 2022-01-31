# https://www.acmicpc.net/problem/6603

import sys


def selNum(sets, nums):
    res = []
    if len(sets) == nums:
        res.append(sets)
        return res
    if nums == 1:
        for s in sets:
            res.append([s])
        return res
    for i, v in enumerate(sets):
        if len(sets) - i == nums - 1:
            break
        temp_res = selNum(sets[i + 1 :], nums - 1)
        for t in temp_res:
            res.append([v] + t)
    return res


def solve():
    input = sys.stdin.readline
    TCs = []
    while True:
        temp = list(map(int, input().split()))
        N = temp[0]
        if N == 0:
            break
        TCs.append(sorted(temp[1:]))

    for TC in TCs:
        res = selNum(TC, 6)
        for r in res:
            print(" ".join(str(x) for x in r))
        print()
    return


if __name__ == "__main__":
    solve()
