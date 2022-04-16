#https://www.acmicpc.net/problem/11727

# 재귀함수 호출 방법1 - Recursion Error 발생
# def step(n): #fail
#     if n not in memo:
#         memo[n] = step(n-1) + 2*step(n-2) 
#     return memo[n]

def solve():
    n = int(input())
    # 풀이 1. 재귀함수 호출
    # global memo
    # memo = {1: 1, 2: 3}
    # res = step(n)
    
    # 풀이 2. DP
    dp = [0]*(n+1)
    for i in range(1,n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 3
        else:
            dp[i] = dp[i-1]+2*dp[i-2]
    res = dp[-1]
    
    return print(res%10007)

if __name__ =="__main__":
    solve()
    