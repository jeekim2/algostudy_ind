# https://www.acmicpc.net/problem/14246


def solve():
    N = int(input())
    Nums = list(map(int, input().split()))
    K = int(input())
    PSum = [0]
    TempSum = 0
    for n in Nums:
        TempSum += n
        PSum.append(TempSum)
    cnt = 0
    for i in range(len(PSum)):
        for j in range(len(PSum) - 1, i, -1):
            if PSum[j] - PSum[i] > K:
                cnt += 1
            else:
                break
    print(cnt)
    return


if __name__ == "__main__":
    solve()
