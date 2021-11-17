# https://www.acmicpc.net/problem/11050
import sys


def Binomial(n, r):
    if r < n // 2:
        r = n - r
    if n == r:
        return 1
    if n - 1 == r:
        return n
    return Binomial(n - 1, r) + Binomial(n - 1, r - 1)
    # nCk = n-1Ck + n-1Ck-1


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    # 이항계수(조합) (N K) 구하기
    # nCk = n! / (k! * (n-k)!)
    print(Binomial(N, K))


if __name__ == "__main__":
    solve()
