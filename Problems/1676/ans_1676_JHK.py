# https://www.acmicpc.net/problem/1676


def solve():
    N = int(input())
    NumFive = N // 5 + N // 25 + N // 125
    print(NumFive)
    return


if __name__ == "__main__":
    solve()
