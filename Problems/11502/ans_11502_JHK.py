# https://www.acmicpc.net/problem/11502

import sys


def get_primeNum_set(PrimeNum, Num):
    for i in range(Num):
        if PrimeNum[i]:
            for j in range(i, Num):
                if PrimeNum[j]:
                    for k in range(j, Num):
                        if PrimeNum[k]:
                            Temp = i + j + k
                            if Temp == Num:
                                return [i, j, k]
                            if Temp > Num:
                                break
    return


def solve():
    input = sys.stdin.readline
    T = int(input())
    TC = []
    for _ in range(T):
        TC.append(int(input()))
    MaxNum = max(TC)
    PrimeNum = [True] * (MaxNum + 1)
    PrimeNum[0] = False
    PrimeNum[1] = False
    for i in range(len(PrimeNum)):
        if PrimeNum[i]:
            j = 2
            while i * j < len(PrimeNum):
                PrimeNum[i * j] = False
                j += 1
    for K in TC:
        print(*get_primeNum_set(PrimeNum, K))
    return


if __name__ == "__main__":
    solve()
