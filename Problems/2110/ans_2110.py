# https://www.acmicpc.net/problem/2110

import sys


def solve():
    input = sys.stdin.readline
    global address
    global installed_list
    N, C = map(int, input().split())
    address = []
    for _ in range(N):
        address.append(int(input()))
    address.sort()

    max_len = (address[-1] - address[0]) // (C - 1) + 1
    min_len = 0

    while min_len + 1 < max_len:
        # check mid is in range
        mid = (min_len + max_len) // 2
        cnt = 1
        last_home = address[0]
        for home in address:
            if home - last_home >= mid:
                last_home = home
                cnt += 1
        if cnt >= C:
            min_len = mid
        else:
            max_len = mid
    print(min_len)


if __name__ == "__main__":
    solve()
