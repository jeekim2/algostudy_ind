# https://www.acmicpc.net/problem/1912

# 예상했던대로 시간초과가 난다

import sys


def solve():
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
            comp[-1] += v
        else:
            comp.append(v)

    if len(comp) == 0:
        # 모두 음수일 때, 최대값 1개만 선택
        print(max(series))
        return
    if len(comp) == 1:
        # 모두 양수일 때
        print(sum(series))
        return

    maxVal = 0
    for i in range(0, len(comp), 2):
        for j in range(i + 1, len(comp), 2):
            temp = sum(comp[i:j])
            if temp > maxVal:
                maxVal = temp
    print(maxVal)
    return


if __name__ == "__main__":
    solve()
