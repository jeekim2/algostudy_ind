# https://www.acmicpc.net/problem/12847


def solve():
    N, M = map(int, input().split())
    T = list(map(int, input().split()))
    j = 0
    TempSum = 0
    MaxSum = 0
    for i in range(N):
        TempSum += T[i]
        j += 1
        if j > M:
            TempSum -= T[i - M]
        MaxSum = max(MaxSum, TempSum)
    print(MaxSum)
    return


if __name__ == "__main__":
    solve()
