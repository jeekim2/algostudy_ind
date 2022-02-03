#https://www.acmicpc.net/problem/11053

def solve0(): #FAIL
    N = int(input())
    values = list(map(int, input().split()))
    dp=[]
    LIS = 0
    for i in range(N-1):
        dp.append(values[i])
        for j in range(i,N):
            if values[j] > dp[-1]:
                dp.append(values[j])
            elif values[j] > dp[j-2]:
                dp[j-2] = values[j]
            else:
                pass            
        LIS = max(LIS, len(dp))
        dp=[]
    print(LIS)
    
def solve1():
    N = int(input())
    values = list(map(int, input().split()))
    dp=[1]*(N)
    
    for i in range(1,N):
        for j in range(i):
            if values[i] > values[j]:
                dp[i] = max(dp[i],dp[j]+1)
    print(max(dp))
                

if __name__=="__main__":
    solve1()