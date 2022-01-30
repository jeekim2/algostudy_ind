#https://www.acmicpc.net/problem/10844

def solve():
    N = int(input())
    #dp[i] = 오름, 중간, 내림
    #dp[i] = [N-i, dp[i-1][1]*2 ,N-i+1]
    #[9,0,0], [8,0,9], [7*2,1,8*2],[6*3,48,7*3], [5,,6] 

    for i in range(N):
        