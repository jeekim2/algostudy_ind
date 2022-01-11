# https://www.acmicpc.net/problem/2579

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    maxScore = {}
    stairs = [0]
    for _ in range(N):
        stairs.append(int(input()))

    if N == 1:
        print(stairs[1])
        return
    if N == 2:
        print(stairs[2] + stairs[1])
        return

    maxScore[1] = [stairs[1], 0]
    maxScore[2] = [stairs[2] + stairs[1], stairs[2]]

    for i in range(3, N + 1):
        # maxScore[i][0]: 한칸 전(i-1)에서 올라왔을 경우의 score
        #    i-1칸을 i-3칸에서 올라와야 함 (연속 금지)
        # maxScore[i][0]: 두칸 전(i-2)에서 올라왔을 경우의 score
        #    i-2칸을 어떻게 도달하건 상관없이 올라올 수 있음 (큰 점수를 획득)
        maxScore[i] = [stairs[i] + maxScore[i - 1][1], stairs[i] + max(maxScore[i - 2])]

    print(max(maxScore[N]))
    return


if __name__ == "__main__":
    solve()
