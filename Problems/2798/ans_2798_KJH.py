# https://www.acmicpc.net/problem/2798


# 이런 식으로 풀면 안되는데 오늘은 술을 먹어야한다.

import sys


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))

    max_sum = 0
    for i in cards:
        for j in cards:
            if j != i:
                for k in cards:
                    if k != j and k != i:
                        temp_sum = i + j + k
                        if max_sum < temp_sum and temp_sum <= M:
                            max_sum = temp_sum

    print(max_sum)


if __name__ == "__main__":
    solve()
