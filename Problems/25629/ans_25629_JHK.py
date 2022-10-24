# https://www.acmicpc.net/problem/25629


def solve():
    N = int(input())
    Nums = list(map(int, input().split()))
    CntOdd = 0
    CntEven = 0
    for v in Nums:
        if v % 2 == 0:
            CntEven += 1
        else:
            CntOdd += 1

    if CntEven == CntOdd:
        print(1)
    elif CntOdd == CntEven + 1:
        print(1)
    else:
        print(0)
    return


if __name__ == "__main__":
    solve()
