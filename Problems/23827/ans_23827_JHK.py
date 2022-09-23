# https://www.acmicpc.net/problem/23827


def solve():
    N = int(input())
    Nums = list(map(int, input().split()))
    PSum = []
    temp = 0
    for v in Nums:
        temp += v
        PSum.append(temp)
    res = 0
    for i, v in enumerate(Nums):
        res = (res + (v * (PSum[-1] - PSum[i]))) % 1000000007
    print(res)
    return


if __name__ == "__main__":
    solve()
