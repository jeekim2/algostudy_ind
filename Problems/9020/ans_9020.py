# https://www.acmicpc.net/problem/9020
"""
골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.
이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.
"""

"""
주석 남겨놓은 내용은 Time out 발생하는 내용.
"""

import sys
from itertools import combinations_with_replacement as combRep


def solve():
    input = sys.stdin.readline
    T = int(input())
    Ns = []
    for _ in range(T):
        Ns.append(int(input()))
    maxN = max(Ns)
    res_sosu = [False, False] + [True] * (maxN - 1)
    for i in range(2, maxN):
        if res_sosu[i]:
            j = 2
            while i * j < maxN:
                res_sosu[i * j] = False
                j += 1

    # for i, v in enumerate(res_sosu):
    #     if v:
    #         sosu.append(i)

    for N in Ns:
        for i in range(N // 2, 1, -1):
            if res_sosu[i] and res_sosu[N - i]:
                print(i, N - i)
                break

        # res = []
        # for i in sosu:
        #     k = N - i
        #     if i < k and k in sosu:
        #         if res:
        #             if res[1] - res[0] > k - i:
        #                 res = [i, k]
        #         else:
        #             res = [i, k]
        # print(res[0], res[1])


if __name__ == "__main__":
    solve()
