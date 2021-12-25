# https://www.acmicpc.net/problem/2565

import sys


def bs(value):
    global l
    left = 0
    right = len(l) - 1
    while right - left > 1:
        mid = (right + left) // 2
        if l[mid] > value:
            right = mid
        elif l[mid] < value:
            left = mid
        elif l[mid] == value:
            return mid
    return right


def solve():
    global tar
    global l

    input = sys.stdin.readline
    N = int(input())
    lines = []
    for _ in range(N):
        lines.append(list(map(int, input().split())))
    lines.sort(key=lambda x: x[0])
    _, tar = zip(*lines)
    l = [0]  # bs에서 0을 return 하지 않으므로(right를 return) default 처리
    for i, v in enumerate(tar):
        if l[-1] < v:
            l.append(v)
        else:
            l[bs(v)] = v
    print(N - len(l) + 1)  # 32번줄의 0의 갯수를 제거하기 위해 +1
    return


if __name__ == "__main__":
    solve()
