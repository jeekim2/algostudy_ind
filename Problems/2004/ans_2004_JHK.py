# https://www.acmicpc.net/problem/2004


def countTwoFive(n):
    MaxN = 2000000000
    cnt2 = 0
    cnt5 = 0
    i = 2
    while i < MaxN:
        cnt2 += n // i
        i *= 2

    i = 5
    while i < MaxN:
        cnt5 += n // i
        i *= 5

    return cnt2, cnt5


def solve():
    N, K = map(int, input().split())
    P = N - K

    N_Cnt2, N_Cnt5 = countTwoFive(N)
    P_Cnt2, P_Cnt5 = countTwoFive(P)
    K_Cnt2, K_Cnt5 = countTwoFive(K)

    Cnt2 = N_Cnt2 - P_Cnt2 - K_Cnt2
    Cnt5 = N_Cnt5 - P_Cnt5 - K_Cnt5

    print(min(Cnt2, Cnt5))
    return


if __name__ == "__main__":
    solve()
