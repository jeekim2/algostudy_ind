# https://www.acmicpc.net/problem/1806


def solve():
    N, S = map(int, input().split())
    Nums = list(map(int, input().split()))
    temp = 0
    PSum = [0]
    for n in Nums:
        temp += n
        PSum.append(temp)
    i = 0
    j = 0
    res = []
    while j < N + 1:
        val = PSum[j] - PSum[i]
        if val < S:
            j += 1
        else:
            res.append(j - i)
            i += 1
    if len(res) == 0:
        print(0)
    else:
        print(min(res))
    return


if __name__ == "__main__":
    solve()
