# https://www.acmicpc.net/problem/1322


def solve():
    X, K = map(int, input().split())
    i = 0
    j = 0
    Y = 0
    while True:
        if (1 << i) & X == 0:
            if K & (1 << j) != 0:
                Y += 1 << i
            j += 1
            if (1 << j) > K:
                break
        i += 1
    print(Y)
    return


if __name__ == "__main__":
    solve()
