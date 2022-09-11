# https://www.acmicpc.net/problem/1789


def solve():
    S = int(input())
    i = 1
    while True:
        if i <= S:
            S -= i
        else:
            print(i - 1)
            return
        i += 1

    return


if __name__ == "__main__":
    solve()
