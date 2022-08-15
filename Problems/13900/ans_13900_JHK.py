# https://www.acmicpc.net/problem/13900


def solve():
    N = int(input())
    Nums = list(map(int, input().split()))
    PSum = []
    TempSum = 0
    for num in Nums:
        TempSum += num
        PSum.append(TempSum)
    res = 0
    for i in range(1, N):
        res += PSum[i - 1] * Nums[i]
    print(res)
    return


if __name__ == "__main__":
    solve()
