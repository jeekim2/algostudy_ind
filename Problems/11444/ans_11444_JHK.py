# https://www.acmicpc.net/problem/11444


# f(N) = f(N-1) + f(N-2)
#     = f(2)* f(N-1) + f(1)* f(N-2)
#     = f(3)*f(N-2) + f(2)*f(N-3)
#     ...
#     = f(m)*f(N-m+1) + f(m-1)*f(N-m)

# when N = 10 (even Number)
# m = 5
# N-m+1 = 6
# m-1 = 4
# N-m = 5

# when N == 11 (odd Number)
# m = 6
# N-m+1 = 6
# m-1 = 5
# N-m = 5


def fiboDiv(N):
    global fibos
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 1
    if N == 3:
        return 2
    if fibos.get(N) == None:
        m = (N + 1) // 2
        # N이 홀수일 때 N//2보다 계산량 감소됨 (위 점화식 분석 참조)
        fibos[N] = (
            fiboDiv(m) * fiboDiv(N - m + 1) + fiboDiv(m - 1) * fiboDiv(N - m)
        ) % 1000000007
    return fibos[N]


def solve():
    global fibos
    fibos = {}
    N = int(input())
    print(fiboDiv(N))


if __name__ == "__main__":
    solve()
