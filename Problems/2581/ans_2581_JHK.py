# https://www.acmicpc.net/problem/2581


def solve():
    M = int(input())
    N = int(input())
    Prime = [True] * (N + 1)
    Prime[0] = False
    Prime[1] = False
    i = 2
    while i < len(Prime):
        if Prime[i]:
            j = 2
            while i * j < len(Prime):
                Prime[i * j] = False
                j += 1
        i += 1
    res = []
    for i, v in enumerate(Prime):
        if i >= M:
            if v:
                res.append(i)
    if res:
        print(sum(res))
        print(res[0])
    else:
        print(-1)
    return


if __name__ == "__main__":
    solve()
