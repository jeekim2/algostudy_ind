# https://www.acmicpc.net/problem/9184

# if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
#     1
# if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
#     w(20, 20, 20)
# if a < b and b < c, then w(a, b, c) returns:
#     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
# otherwise it returns:
#     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

# 위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)
# a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.

import sys


def w_org(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b and b < c:
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    return (
        w(a - 1, b, c)
        + w(a - 1, b - 1, c)
        + w(a - 1, b, c - 1)
        - w(a - 1, b - 1, c - 1)
    )


def w(a, b, c):
    global dic
    if dic.get((a, b, c)) != None:
        # dic 의 값이 0일 경우(나오는지는 모르겠지만), 조건문 False 가능하므로 None이 아닌 경우를 정의
        return dic[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        dic[(20, 20, 20)] = w(20, 20, 20)
        return dic[(20, 20, 20)]
    if a < b and b < c:
        # dic[(a, b, c - 1)] = w(a, b, c - 1)
        # dic[(a, b - 1, c - 1)] = w(a, b - 1, c - 1)
        # dic[(a, b - 1, c)] = w(a, b - 1, c)
        # 이게 더 빠를거같았는데 느리더라...1
        dic[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dic[(a, b, c)]
    # dic[(a - 1, b, c)] = w(a - 1, b, c)
    # dic[(a - 1, b - 1, c)] = w(a - 1, b - 1, c)
    # dic[(a - 1, b, c - 1)] = w(a - 1, b, c - 1)
    # dic[(a - 1, b - 1, c - 1)] = w(a - 1, b - 1, c - 1)
    # 이게 더 빠를거같았는데 느리더라...2
    dic[(a, b, c)] = (
        w(a - 1, b, c)
        + w(a - 1, b - 1, c)
        + w(a - 1, b, c - 1)
        - w(a - 1, b - 1, c - 1)
    )
    return dic[(a, b, c)]


def solve():
    global dic
    dic = {}
    input = sys.stdin.readline
    TCs = []
    while True:
        tempInput = list(map(int, input().split()))
        if tempInput != [-1, -1, -1]:
            TCs.append(tempInput)
        else:
            break
    for TC in TCs:
        a, b, c = TC
        print((f"w({a}, {b}, {c}) = ") + str(w(a, b, c)))
    return


if __name__ == "__main__":
    solve()
