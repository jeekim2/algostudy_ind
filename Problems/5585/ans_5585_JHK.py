# https://www.acmicpc.net/problem/5585


def solve():
    N = 1000 - int(input())
    Coins = [500, 100, 50, 10, 5, 1]
    cnt = 0
    for c in Coins:
        while N >= c:
            N -= c
            cnt += 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
