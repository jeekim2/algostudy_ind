# https://www.acmicpc.net/problem/3036

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    circles = list(map(int, input().split()))
    main_c = circles.pop(0)

    ans = []
    for sub_c in circles:
        # 유클리드 호제법을 이용한 최대공약수 계산
        p = main_c
        q = sub_c
        while True:
            p, q = q, p % q
            if q == 0:
                break
        ans.append([main_c // p, sub_c // p])

    for a in ans:
        print("/".join(list(map(str, a))))


if __name__ == "__main__":
    solve()
