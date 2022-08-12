# https://www.acmicpc.net/problem/1644


def cnt_primeSum(PartialSum, N):
    cnt = 0
    i = 0
    j = 0
    while i < len(PartialSum) and j < len(PartialSum):
        res = PartialSum[j] - PartialSum[i]
        if res == N:
            cnt += 1
            i += 1
            j = i + 1
        elif res > N:
            i += 1
            j = i + 1
        else:
            j += 1
    return cnt


def solve():
    N = int(input())
    PNum = [True] * (N + 1)
    PNum[0] = False
    PNum[1] = False
    for p in range(len(PNum)):
        if PNum[p]:
            i = 2
            while p * i < len(PNum):
                PNum[p * i] = False
                i += 1
    PartialSum = [0]
    TempSum = 0
    for i, v in enumerate(PNum):
        if v:
            TempSum += i
            PartialSum.append(TempSum)
    print(cnt_primeSum(PartialSum, N))
    return


if __name__ == "__main__":
    solve()
