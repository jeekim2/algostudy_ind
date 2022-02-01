#https://www.acmicpc.net/problem/2193

def solve():
    N = int(input())
    
    dp=[0 for _ in range(N+1)]
    if N < 3:
        dp[N] = 1
    else:
        dp[1], dp[2] = 1, 1
        for i in range(3,N+1):
            dp[i] = dp[i-1]+dp[i-2]
    print(dp[N])

if __name__ == "__main__":
    solve()