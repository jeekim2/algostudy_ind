# https://www.acmicpc.net/problem/11051

import sys


def solve():
    DIV = 10007
    input = sys.stdin.readline
    N, K = map(int, input().split())
    # 11050 문제와 같이 재귀로 풀면 N이 큰 경우에 대해 재귀 제한에 걸려서 불가능
    # Memory 제한조건이 256MB이므로, Bottom-up으로 주어진 Range에 대해 조합 테이블을 생성하기 충분
    # Python은 Overflow가 존재하지 않으므로 Factorial 계산을 해버려도 무방하지만...
    # nCk = n-1Ck + n-1Ck-1
    nCr = {}
    nCr[(1, 0)] = 1
    nCr[(1, 1)] = 1

    for i in range(1, N + 1):
        for j in range(i + 1):
            if i - 1 < 2 * j:
                j = i - j
            if j == 1:
                nCr[(i, j)] = i
            elif j == 0:
                nCr[(i, j)] = 1
            else:
                # 이부분 머리아파서 정리가 안됨... 걍 빡코딩

                try:
                    t1 = nCr[(i - 1, j - 1)]
                except:
                    t1 = nCr[(i - 1, i - j)]
                try:
                    t2 = nCr[(i - 1, j)]
                except:
                    t2 = nCr[(i - 1, i - j - 1)]
                nCr[(i, j)] = (t1 + t2) % DIV

    print(nCr[(N, K)] % DIV)


if __name__ == "__main__":
    solve()
