# https://www.acmicpc.net/problem/2156

# 10844 문제와 거의 유사하나, 세부 조건이 다름.
# 1. 마지막 와인을 안마셔도 됨
# 2. 건너뛰는 와인의 갯수 제한이 없음
# -> 최대 2개를 건너 뛰는 경우를 고려해야함
# -> 3개를 건너뛰어야 하는 경우, 1개 pass - 1개 선택 - 1개 pass가 더 효율적

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    wines = []
    score = {}
    for _ in range(N):
        wines.append(int(input()))
    if N == 1 or N == 2:
        print(sum(wines))
        return
    # score[] : [직전 와인을 선택하지 않은 경우 최대 점수, 직전 와인을 선택 한 경우 최대 점수]
    score[0] = [wines[0], wines[0]]
    score[1] = [wines[1], wines[1] + wines[0]]
    score[2] = [wines[2] + wines[0], wines[2] + wines[1]]
    for i in range(3, N):
        score[i] = [
            wines[i] + max(max(score[i - 2]), max(score[i - 3])),
            wines[i] + score[i - 1][0],
        ]

    print(max(max(score[N - 1]), max(score[N - 2]), max(score[N - 3])))
    return


if __name__ == "__main__":
    solve()
