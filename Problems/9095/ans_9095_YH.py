#https://www.acmicpc.net/problem/9095

#Bottom-Up 방식
def solve1():
    T = int(input())
    dp = [0]*11 # 테스트 케이스 input의 최대값이 11 (문제 조건)
    dp[1], dp[2], dp[3] = 1, 2, 4 # 초기값 설정
    for _ in range(T):
        TC = int(input())
        for x in range(4,TC+1):
            dp[x] = sum([dp[x-1], dp[x-2], dp[x-3]]) # 1,2,3 계단 오르는 문제와 비슷
        print(dp[TC])

#Top-Down 방식
def solve2():
    T = int(input())
    global memo
    memo = {1:1, 2:2, 3:4} #초기값 설정
    for _ in range(T):
        TC = int(input())
        print(dp(TC))
def dp(n):
    if n not in memo:
        result = dp(n-1)+dp(n-2)+dp(n-3) # 1,2,3 계단 오르는 점화식과 동일
        memo[n] = result
        return result
    return memo[n]

if __name__ == "__main__":
    solve1() #Bottom-up
    solve2() #Top-down