# https://softeer.ai/practice/info.do?idx=1&eid=628

import sys


def bs(usage, resource, left):
    right = len(usage) - 1
    while right - left > 1:
        mid = (right + left) // 2
        if usage[mid] <= resource:
            right = mid
        else:
            left = mid
    return left


def set_usage(usage, is_visisted, resource, startidx):
    if startidx >= len(usage):
        return
    idx = bs(usage, resource, startidx)
    for i in range(idx, len(usage)):
        if not is_visisted[i]:
            if usage[i] < resource:
                is_visisted[i] = True
                set_usage(usage, is_visisted, resource - usage[i], i + 1)
                return
            if usage[i] == resource:
                is_visisted[i] = True
                return


def cnt_server(usage):
    cnt = 0
    is_visisted = [False] * len(usage)
    for i in range(len(usage)):
        if not is_visisted[i]:
            cnt += 1
            reserved = 900
            is_visisted[i] = True
            set_usage(usage, is_visisted, reserved - usage[i], i + 1)

    return cnt


def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = []
    for _ in range(N):
        _ = int(input())
        TC.append(list(map(int, input().split())))
    cnt = 0
    for t in TC:
        t.sort(reverse=True)
        print(cnt_server(t))
    return


if __name__ == "__main__":
    solve()
