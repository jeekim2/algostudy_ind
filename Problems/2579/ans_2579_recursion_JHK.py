# https://www.acmicpc.net/problem/2579

import sys


def getMax(idx):
    global stairs
    global maxScore
    if idx in maxScore:
        return maxScore[idx]
    if idx == 1:
        maxScore[idx] = [stairs[1], stairs[1]]
        return maxScore[idx]
    if idx == 2:
        maxScore[idx] = [stairs[2] + stairs[1], stairs[2]]
        return maxScore[idx]
    stair1Before = getMax(idx - 1)
    stair2Before = getMax(idx - 2)
    maxScore[idx] = [stairs[idx] + stair1Before[1], stairs[idx] + max(stair2Before)]
    return maxScore[idx]
    # return[0]: 한칸 전(i-1)에서 올라왔을 경우의 score
    #    i-1칸을 i-3칸에서 올라와야 함 (연속 금지)
    # return[1]: 두칸 전(i-2)에서 올라왔을 경우의 score
    #    i-2칸을 어떻게 도달하건 상관없이 올라올 수 있음 (큰 점수를 획득)
    # maxScore[i] = [stairs[i] + maxScore[i - 1][1], stairs[i] + max(maxScore[i - 2])]


def solve():
    global stairs
    global maxScore
    input = sys.stdin.readline
    N = int(input())
    maxScore = {}
    stairs = [0]
    for _ in range(N):
        stairs.append(int(input()))

    print(max(getMax(N)))
    # 마지막 계단에 반드시 도달해야함.

    return


if __name__ == "__main__":
    solve()
