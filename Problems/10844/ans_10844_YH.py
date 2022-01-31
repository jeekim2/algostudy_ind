#https://www.acmicpc.net/problem/10844
#참조 풀이임... 머리속에 멤도는 점화식을 풀이로 담아내는 게 아직도 부족...

def solve():
    N = int(input())
    #dp[i][j] : 계단수 길이가 i고, 끝자리가 j로 끝나는 경우의 갯수
    dp=[[0,0,0,0,0,0,0,0,0,0] for _ in range(N+1)] 
    dp[1] = [0,1,1,1,1,1,1,1,1,1]
    
    for i in range(2, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1] 
    print(sum(dp[N])%10**9)
    
if __name__ == "__main__":
    solve()