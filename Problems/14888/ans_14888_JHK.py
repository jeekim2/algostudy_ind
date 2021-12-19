# https://www.acmicpc.net/problem/14888

import sys


def OpCal(idx):
    global N
    global A
    global opCnt
    global ans, ansList
    if idx < N:
        temp = A[idx]
        ansBefore = ans
        for i in range(4):  # OP
            if opCnt[i] != 0:
                if i == 0:  # +
                    ans = ansBefore + temp
                elif i == 1:  # -
                    ans = ansBefore - temp
                elif i == 2:  # *
                    ans = ansBefore * temp
                else:  # /
                    # 나눗셈은 정수 나눗셈으로 몫만 취한다.
                    if ansBefore < 0:
                        # 음수를 양수로 나눌 때는 C++14의 기준을 따른다.
                        # 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
                        ans = -((-ansBefore) // temp)
                    else:
                        ans = ansBefore // temp
                opCnt[i] -= 1
                OpCal(idx + 1)
                ans = ansBefore
                opCnt[i] += 1
    else:
        ansList.append(ans)


def solve():
    global N
    global A
    global opCnt
    global ans, ansList
    N = int(input())
    A = list(map(int, input().split()))
    opCnt = list(map(int, input().split()))
    ansList = []
    ans = A[0]
    OpCal(1)

    print(max(ansList))
    print(min(ansList))

    return


if __name__ == "__main__":
    solve()
