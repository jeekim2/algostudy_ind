# https://www.acmicpc.net/problem/17626


def solve():
    N = int(input())
    dp = [50001] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            val = j * j
            if val > i:
                break
            dp[i] = min(dp[i], dp[i - val] + 1)
    print(dp[N])
    return


if __name__ == "__main__":
    solve()
