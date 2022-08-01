# https://www.acmicpc.net/problem/15736


def solve():
    N = int(input())
    cnt = 0
    res = 0
    i = 1
    while True:
        res = i * i
        if res <= N:
            cnt += 1
        else:
            print(cnt)
            return
        i += 1


if __name__ == "__main__":
    solve()
