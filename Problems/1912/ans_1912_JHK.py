# https://www.acmicpc.net/problem/1912

import sys


def getMax(idx):
    global dic
    global comp
    if idx in dic:
        return dic[idx]
    if idx + 1 >= len(comp):
        dic[idx] = comp[idx]
        return dic[idx]
    temp = comp[idx + 1] + getMax(idx + 2)
    if temp > 0:
        dic[idx] = comp[idx] + temp
    else:
        dic[idx] = comp[idx]
    return dic[idx]


def solve():
    global dic
    global comp
    dic = {}
    input = sys.stdin.readline
    N = int(input())
    series = list(map(int, input().split()))
    comp = []
    # 연속된 양수, 연속된 음수를 모두 더해 하나로 압축, 짝수번은 항상 양수
    for v in series:
        if comp == []:
            if v > 0:
                comp.append(v)
        elif (v >= 0 and comp[-1] > 0) or (v <= 0 and comp[-1] < 0):
            # v > 0, v < 0이 아님에 주의
            # ex1. ... -1 2 0 3 -4 ...
            # ex2. ... 2 -3 0 -4 5 ...
            # 0을 끼고서도 compression이 되어야 함.
            comp[-1] += v
        else:
            comp.append(v)

    if len(comp) == 0:
        # 모두 음수일 때, 최대값 1개만 선택
        print(max(series))
        return
    if len(comp) == 1:
        # 모두 양수일 때
        print(sum(comp))
        return

    if comp[-1] < 0:
        comp.pop()
        # 아래 for문 간단하게 만들기 위함.
    for i in range(len(comp) - 1, -1, -2):
        getMax(i)
        # for문 없이 getMax(0) 처리해도 무방하나, comp가 길어지면 recursion 제한에 걸림.

    print(max(dic.values()))
    return


if __name__ == "__main__":
    solve()
