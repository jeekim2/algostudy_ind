# https://www.acmicpc.net/problem/1094


def solve():
    N = int(input())
    bN = bin(N)
    print(bN.count("1"))
    return


if __name__ == "__main__":
    solve()
