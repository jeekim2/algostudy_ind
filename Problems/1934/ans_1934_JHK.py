# https://www.acmicpc.net/problem/14391


def gcd(A, B):
    if A < B:
        A, B = B, A
    while B != 0:
        A, B = B, A % B
    return A


def solve():
    T = int(input())
    TC = [tuple(map(int, input().split())) for _ in range(T)]
    for A, B in TC:
        print(A * B // gcd(A, B))
    return


if __name__ == "__main__":
    solve()
