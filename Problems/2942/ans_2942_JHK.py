# https://www.acmicpc.net/problem/2942


def get_GCD(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def get_divs(n):
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res


def solve():
    R, G = map(int, input().split())
    gcd = get_GCD(R, G)
    divs = get_divs(gcd)
    for d in divs:
        print(d, R // d, G // d)
    return


if __name__ == "__main__":
    solve()
