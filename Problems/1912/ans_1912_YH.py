#https://www.acmicpc.net/problem/1912

def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    dp=[-1000]*n #dp[i] : i번째에서 최대값인 경우
    dp[0]=numbers[0]
    for i in range(1,n):
        dp[i] = max(numbers[i],dp[i-1]+numbers[i])
    
    #print(dp)
    print(max(dp))

if __name__=="__main__":
    solve()