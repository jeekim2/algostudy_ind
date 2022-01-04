# https://www.acmicpc.net/problem/9375

import sys


def matchPassion(TC):
    clothes = {}
    for cloth in TC:
        if clothes.get(cloth[1]):
            clothes[cloth[1]].add(cloth[0])
        else:
            clothes[cloth[1]] = {cloth[0]}
            # set 으로 시작

    selectNumbers = 1
    for TypedWears in clothes.values():
        selectNumbers *= len(TypedWears) + 1
        # 해당 의상 종류에서 아무것도 선택되지 않을 경우를 +1
    print(selectNumbers - 1)
    # 모든 의상을 입지 않을 경우를 제외

    return


def solve():
    T = int(input())
    TCs = []
    for _ in range(T):
        TC = []
        N = int(input())
        for _ in range(N):
            TC.append(input().split())
        TCs.append(TC)

    for TC in TCs:
        matchPassion(TC)
    return


if __name__ == "__main__":
    solve()
