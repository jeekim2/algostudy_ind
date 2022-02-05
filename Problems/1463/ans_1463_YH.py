#https://www.acmicpc.net/problem/1463

# Bottom-Up 방식
def solve1():
    N = int(input())
    dp = [0]*(N+1) #초기화, dp[n] - 입력 n에 대한 연산 횟수의 최소값
    if N == 1:
        print(dp[1])
    else:
        dp[2] = 1
        for i in range(3,N+1):
            if i%2 == 0 and i%3 == 0: # 2와 3의 배수(간과하기 쉬울듯..)
                dp[i] = min(dp[i//3], dp[i//2], dp[i-1])+1
            elif i%3 == 0:
                dp[i] = min(dp[i//3], dp[i-1])+1
            elif i%2 == 0:
                dp[i] = min(dp[i//2], dp[i-1])+1
            else:
                dp[i] = dp[i-1]+1
        print(dp[N])

# Top-Down 방식
def solve2():
    N = int(input())
    global memo
    memo = {1:0, 2:1}
    print(dp(N))

def dp(n):
    if n not in memo : 
        result = min(dp(n//3)+n%3, dp(n//2)+n%2)+1 # 3계단 또는 2계단 또는 1계단 오르는 계단 오르기 문제와 비슷
        memo[n] = result
        return result
    return memo[n]

if __name__ == "__main__":
    solve1()
    solve2()
