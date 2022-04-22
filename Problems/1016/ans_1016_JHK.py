# https://www.acmicpc.net/problem/1016


def solve():
    MinVal, MaxVal = map(int, input().split())
    Res = [1] * (MaxVal - MinVal + 1)
    i = 1
    while i ** 2 < MaxVal:
        i += 1
        doubleI = i ** 2
        IdxVal = (MaxVal // doubleI) * doubleI
        while IdxVal >= MinVal:
            if Res[IdxVal - MinVal]:
                Res[IdxVal - MinVal] = 0
            IdxVal -= doubleI

    print(sum(Res))
    return


if __name__ == "__main__":
    solve()
