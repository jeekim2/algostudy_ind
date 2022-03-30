# https://www.acmicpc.net/problem/2559


def solve():
    N, K = map(int, input().split())
    TempList = list(map(int, input().split()))

    TempSum = 0
    for i in range(K):
        TempSum += TempList[i]
    MaxTempSum = TempSum
    i = 0
    while i + K < N:
        TempSum -= TempList[i]
        TempSum += TempList[i + K]
        if TempSum > MaxTempSum:
            MaxTempSum = TempSum
        i += 1
    print(MaxTempSum)
    return


if __name__ == "__main__":
    solve()
