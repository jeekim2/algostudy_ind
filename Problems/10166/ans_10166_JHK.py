# https://www.acmicpc.net/problem/10166


def solve():
    D1, D2 = map(int, input().split())
    res = set()
    res.add((0, 0))
    for v in range(D1, D2 + 1):
        for a in range(1, v):
            p = a
            b = v
            while b % a != 0:
                a, b = b % a, a
            res.add((v // a, p // a))
    print(len(res))
    return


if __name__ == "__main__":
    solve()
