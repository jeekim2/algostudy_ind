# https://www.acmicpc.net/problem/1149

import sys

"""
def greedy(homes):
    # 이렇게 풀면 안되더라를 남김
    priceSum = 0
    for i, home in enumerate(homes):
        if i == 0:
            selected = home.index(min(home))
            priceSum += min(home)
        else:
            if selected == 0:
                if home[1] < home[2]:
                    selected = 1
                    priceSum += home[1]
                else:
                    selected = 2
                    priceSum += home[2]
            elif selected == 1:
                if home[0] < home[2]:
                    selected = 0
                    priceSum += home[0]
                else:
                    selected = 2
                    priceSum += home[2]
            else:
                if home[0] < home[1]:
                    selected = 0
                    priceSum += home[0]
                else:
                    selected = 1
                    priceSum += home[1]
    print(priceSum)
"""


def checkMin(startHome, startColor):
    # 재귀를 이용해 dictionary를 채우는 방식으로 하면, Home이 많아질 경우 Recuresion error 발생 (너무 깊음)
    global homes
    global dic
    if dic.get((startHome, startColor)):
        return dic[(startHome, startColor)]
    if startHome == len(homes):
        return 0
    if startColor == 0:
        dic[(startHome, startColor)] = homes[startHome][startColor] + min(
            checkMin(startHome + 1, 1), checkMin(startHome + 1, 2)
        )
    if startColor == 1:
        dic[(startHome, startColor)] = homes[startHome][startColor] + min(
            checkMin(startHome + 1, 0), checkMin(startHome + 1, 2)
        )
    if startColor == 2:
        dic[(startHome, startColor)] = homes[startHome][startColor] + min(
            checkMin(startHome + 1, 0), checkMin(startHome + 1, 1)
        )
    return dic[(startHome, startColor)]


def solve():
    global homes
    global dic
    dic = {}
    input = sys.stdin.readline
    N = int(input())
    homes = []
    for _ in range(N):
        homes.append(list(map(int, input().split())))

    # 집 갯수가 적은 경우, checkMin 함수의 재귀 자체로서 dictionary를 채워넣을 수 있으나...
    # (76번줄 for 문 없이도, 아래 print문 자체로서 Ok)
    # print(min(checkMin(0, 0), checkMin(0, 1), checkMin(0, 2)))

    for i in range(len(homes), -1, -1):
        # checkMin에서 재귀가 발생하지 않게 하기 위해서,
        # 제일 깊은것부터 순차적으로 미리 호출하여 dictionary를 채워넣음.
        checkMin(i, 0)
        checkMin(i, 1)
        checkMin(i, 2)

    print(min(checkMin(0, 0), checkMin(0, 1), checkMin(0, 2)))
    return


if __name__ == "__main__":
    solve()
