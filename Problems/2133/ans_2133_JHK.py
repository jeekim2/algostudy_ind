# https://www.acmicpc.net/problem/2133


def solve():
    N = int(input())
    if N % 2 != 0:
        print(0)
        return
    Memo = [0] * (max(6, N) + 1)
    Memo[2] = 3
    Memo[4] = 11
    for i in range(6, N + 1, 2):
        Memo[i] = 4 * Memo[i - 2] - Memo[i - 4]
    print(Memo[N])
    return


if __name__ == "__main__":
    solve()
