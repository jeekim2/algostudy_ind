#  동적 계획법으로 재귀 횟수 줄이기
def fibo(N):
    global d
    if d.get(N) == None:
        if N == 0:
            d[N] = [1, 0, 0]
        elif N == 1:
            d[N] = [0, 1, 1]
        else:
            d[N] = [sum(x) for x in zip(fibo(N - 1), fibo(N - 2))]
    return d[N]


def solve():
    global d
    d = {}
    N = int(input())
    res = []
    for _ in range(N):
        t = int(input())
        fibo(t)
        res.append(t)
    for r in res:
        print(d[r][0], d[r][1])


if __name__ == "__main__":
    solve()
