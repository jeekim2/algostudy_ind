# https://www.acmicpc.net/problem/14889

import sys
from itertools import combinations


# 결과적으로, 로직 구현한 것이 combinations 시간효율을 따라가지 못함.
# 빡센 문제인듯.


def sum_teamScore(team):
    global score
    sum = 0
    for t in combinations(team, 2):
        sum += score[t[0]][t[1]] + score[t[1]][t[0]]

    # for i in team:
    #     for j in team:
    #         if i > j:
    #             sum += score[i][j] + score[j][i]
    return sum


def comp_teams():
    global memb, total_id, ans_min
    for team_a in memb:
        team_b = list(total_id - set(team_a))
        score_gap = abs(sum_teamScore(team_a) - sum_teamScore(team_b))
        ans_min = min(ans_min, score_gap)
    return


def select_members(depth, init_val):
    global memb, temp_memb

    if depth >= N // 2:
        memb.append(temp_memb.copy())
        return

    for i in range(init_val, N):
        temp_memb.append(i)
        select_members(depth + 1, i + 1)
        del temp_memb[-1]

    return


def select_members2(k):
    global memb, temp_memb
    global is_not_visited
    if k == N // 2:
        memb.append(temp_memb.copy())
        return
    for i in range(N):
        if is_not_visited[i]:
            temp_memb[k] = i
            is_not_visited[0:i] = [False for j in range(i + 1)]
            select_members2(k + 1)
            is_not_visited[i + 1] = True
    return


def solve():
    input = sys.stdin.readline
    global N, score, memb, temp_memb, total_id, ans_min
    global is_not_visited
    N = int(input())
    score = []
    for _ in range(N):
        score.append(list(map(int, input().split())))
    memb = []
    temp_memb = [0] * (N // 2)
    # temp_memb = []
    is_not_visited = [True] * N
    total_id = set([x for x in range(N)])
    ans_min = 100 * N

    # itertools 보다 효율적인 코드가 나오질 않음...
    # select_members(0, 0)
    # select_members2(0)
    memb = list(combinations([x for x in range(N)], N // 2))

    # remove가 시간이 꽤 걸린다 - 시간초과 요인
    # for team in memb:
    #     memb.remove(tuple(total_id - set(team)))
    # comp_teams()

    for team_a in memb:
        sum_a = 0
        sum_b = 0
        team_b = list(total_id - set(team_a))

        for t in combinations(team_a, 2):
            sum_a += score[t[0]][t[1]] + score[t[1]][t[0]]

        for t in combinations(team_b, 2):
            sum_b += score[t[0]][t[1]] + score[t[1]][t[0]]

        score_gap = abs(sum_a - sum_b)
        if ans_min > score_gap:
            ans_min = score_gap

    print(ans_min)
    return


if __name__ == "__main__":
    solve()
