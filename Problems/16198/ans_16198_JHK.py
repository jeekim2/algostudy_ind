# https://www.acmicpc.net/problem/16198

import itertools


def get_Energy(Cores, select):
    is_visited = [False] * len(Cores)
    res = 0
    for i in select:
        is_visited[i] = True
        j = i - 1
        while is_visited[j]:
            j -= 1
        k = i + 1
        while is_visited[k]:
            k += 1
        res += Cores[j] * Cores[k]
    return res


def solve():
    N = int(input())
    BaseSel = [x for x in range(1, N - 1)]
    Cores = list(map(int, input().split()))
    Selects = list(itertools.permutations(BaseSel, N - 2))
    MaxEnergy = 0
    for sel in Selects:
        MaxEnergy = max(MaxEnergy, get_Energy(Cores, sel))
    print(MaxEnergy)
    return


if __name__ == "__main__":
    solve()
