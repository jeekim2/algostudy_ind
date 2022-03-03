# https://www.acmicpc.net/problem/10837

import sys


def check_avail(M, N, K):
    if M > N:
        # K판 중 M판을 수행, 영희가 M판을 모두 이긴 상태를 가정.
        # 동수는 아직 던지지 않은 상태로 N점을 획득한 상태.
        # M판보다 더 수행한 경우(영희가 점수를 얻지 못한 판이 있을 경우),
        # 동수가 앞으로 얻을 수 있는 기댓값이 작아짐.
        # 즉, 상기 가정은 동수에게 최대한 유리한 경우를 따질 수 있는 상태.
        if M - 1 <= N + K - M + 1:
            # 상기 가정 중, M-1판째 동수가 N점을 획득한 상태에서,
            # 다음경기 (M번째 판)가 지속될 수 있는지를 확인
            # 동수가 앞으로 얻을 수 있는 점수가 영희의 현재 점수 (M-1) 보다 크거나 같아야 게임 지속
            return 1
    if M < N:
        # K판 중 N판을 수행, 동수가 N판을 모두 이긴 상태를 가정.
        # 영희가 먼저 던지므로 영희는 N판 중 M점을 획득함.
        # 동수가 N번째 판을 던지기 바로 전(N-1점), 게임이 지속될 수 있는지 확인
        if M + K - N >= N - 1:
            # 영희가 앞으로 얻을 수 있는 기댓값이 현재 동수의 점수보다 크거나 같아야 게임 지속
            return 1
    if M == N:
        return 1
    return 0


def solve():
    input = sys.stdin.readline
    K = int(input())
    C = int(input())
    TC = []
    for _ in range(C):
        TC.append(list(map(int, input().split())))

    for T in TC:
        print(check_avail(*T, K))

    return


if __name__ == "__main__":
    solve()
