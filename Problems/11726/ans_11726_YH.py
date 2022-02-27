#https://www.acmicpc.net/problem/11726
#결국 1계단 또는 2계단으로 계단 오르기와 같음

#Bottom-Up
def solve1():
    N = int(input())
    dp = [0]*1001
    dp[1], dp[2] = 1, 2
    for i in range(3,N+1):
        dp[i] = dp[i-1]+dp[i-2]
    print(dp[N]%10007)
    
#Top-Down
#메모이제이션 적용해도 입력 최대 1000에 따른 Recursion 1000 초과됨에 따라 Recursion Error발생(백준 기준)
# --> 지환이형 조언에 따라 아래서부터 호출하는 풀이로 Pass
def solve2():
    N = int(input())
    global memo
    memo = {0:0, 1:1, 2:2}
    
    i=3
    while i<N:
        dp(i)
        i+=1
    print(dp(N)%10007)
        
    
def dp(n):
    if n <=2 :
        memo[n] = n
    else:
        if n not in memo:
            result = dp(n-1)+dp(n-2)
            memo[n] = result
    return memo[n]

if __name__=="__main__":
    #solve1()
    solve2()