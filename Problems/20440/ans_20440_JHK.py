# https://www.acmicpc.net/problem/20440

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    Enter = []
    Exit = []

    for _ in range(N):
        s, e = map(int, input().split())
        Enter.append(s)
        Exit.append(e)
    Enter = sorted(Enter)
    Exit = sorted(Exit)
    i = 0
    j = 0
    t = 0
    MaxNum = 0
    CurNum = 0
    Iscont = False
    while i < len(Enter) and j < len(Enter):
        if Enter[i] == Exit[j]:
            i += 1
            j += 1
        elif Enter[i] < Exit[j]:
            CurNum += 1
            if CurNum > MaxNum:
                MaxNum = CurNum
                Iscont = True
                Tem = Enter[i]
            i += 1
        else:
            if CurNum == MaxNum:
                if Iscont:
                    Txm = Exit[j]
            CurNum -= 1
            j += 1
            Iscont = False
    while i < len(Enter):
        if Enter[i] == Exit[-1]:
            i += 1
        else:
            CurNum += 1
            if CurNum > MaxNum:
                MaxNum = CurNum
                Iscont = True
                Tem = Enter[i]
            i += 1
    while j < len(Enter):
        if Enter[-1] == Exit[j]:
            j += 1
        else:
            if CurNum == MaxNum:
                if Iscont:
                    Txm = Exit[j]
            CurNum -= 1
            j += 1
            Iscont = False
    print(MaxNum)
    print(Tem, Txm)
    return


if __name__ == "__main__":
    solve()
