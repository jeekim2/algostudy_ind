# https://www.acmicpc.net/problem/11729


# 재귀함수 구현 할 때 고려사항
# 1. 해당 함수 호출의 의미
# 2. 그 호출에서 재귀호출을 할 때의 관계
# 호출을 따라가면서 생각하려 하지 말 것

import sys


def moveHanoi(N, fromPoll, ToPoll):
    # N개의 판을 fromPoll 에서 ToPoll로 옮기는 함수
    global res
    if N == 1:
        res.append((fromPoll, ToPoll))
        return
    BufferPoll = 6 - fromPoll - ToPoll
    moveHanoi(N - 1, fromPoll, BufferPoll)
    # 먼저 N-1 개 판을 BufferPoll로 옮겨둔 후
    # (BufferPoll로 옮기기 위해, ToPoll 을 경유하는 것은 재귀에 맞긴다)
    res.append((fromPoll, ToPoll))
    # 마지막 판을 ToPoll로 옮기고
    moveHanoi(N - 1, BufferPoll, ToPoll)
    # BufferPoll에 두었던 N-1개 판을 ToPoll로 옮긴다
    return


def solve():
    N = int(input())
    global res
    res = []
    moveHanoi(N, 1, 3)
    print(len(res))
    for i in res:
        print(i[0], i[1])
    return


if __name__ == "__main__":
    solve()
