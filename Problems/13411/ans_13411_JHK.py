# https://www.acmicpc.net/problem/13411

import sys


def sort_robot(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]:
                res.append(left[i])
                i += 1
            elif left[i][1] > right[j][1]:
                res.append(right[j])
                j += 1
            else:
                if left[i][0] < right[j][0]:
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

    return merge(sort_robot(arr[: len(arr) // 2]), sort_robot(arr[len(arr) // 2 :]))


def solve():
    input = sys.stdin.readline
    N = int(input())
    Robots = []
    ID = 1
    for _ in range(N):
        x, y, v = map(int, input().split())
        Robots.append((ID, ((x**2 + y**2) ** 0.5) / v))
        ID += 1
    sortedRobot = sort_robot(Robots)
    for r in sortedRobot:
        ID, Val = r
        print(ID)
    return


if __name__ == "__main__":
    solve()
