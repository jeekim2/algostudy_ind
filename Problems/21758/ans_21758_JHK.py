# https://www.acmicpc.net/problem/21758


def get_between_sum(s, e, PSum):
    return PSum[e] - PSum[s]


def solve():
    N = int(input())
    Honey = list(map(int, input().split()))
    PSum = []
    tempSum = 0
    for h in Honey:
        tempSum += h
        PSum.append(tempSum)
    HoneyMax = 0
    # Bee - Bee - House
    DefHoney = Honey[N - 1] + PSum[N - 1] - PSum[0]
    for i in range(1, N - 1):
        SecondHoney = PSum[N - 2] - PSum[i] - Honey[i]
        if HoneyMax < DefHoney + SecondHoney:
            HoneyMax = DefHoney + SecondHoney

    # House - Bee - Bee
    DefHoney = PSum[N - 2]
    for i in range(1, N - 1):
        SecondHoney = PSum[i - 1] - Honey[i]
        if HoneyMax < DefHoney + SecondHoney:
            HoneyMax = DefHoney + SecondHoney

    # Bee - House - Bee
    DefHoney = PSum[N - 2] - PSum[0]
    for i in range(1, N - 1):
        if HoneyMax < DefHoney + Honey[i]:
            HoneyMax = DefHoney + Honey[i]
    print(HoneyMax)
    return


if __name__ == "__main__":
    solve()
