# https://www.acmicpc.net/problem/1193


def solve():
    N = int(input())
    i = 1
    tempN = N
    while i < tempN:
        tempN -= i
        i += 1
    if i % 2 == 0:
        a = tempN
        b = i + 1 - tempN
    else:
        a = i + 1 - tempN
        b = tempN
    print(f"{a}/{b}")
    return


if __name__ == "__main__":
    solve()
