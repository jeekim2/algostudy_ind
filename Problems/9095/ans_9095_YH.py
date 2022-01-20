#https://www.acmicpc.net/problem/9095

#Bottom-Up 방식
def solve():
    T = int(input())
    dp = [0]*11
    dp[1], dp[2], dp[3] = 1, 2, 4
    for _ in range(T):
        TC = int(input())
        for x in range(4,TC+1):
            dp[x] = sum([dp[x-1], dp[x-2], dp[x-3]])
        print(dp[TC])

if __name__ == "__main__":
    solve()