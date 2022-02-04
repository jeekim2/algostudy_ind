#https://www.acmicpc.net/problem/11053

# Dynamic Programming   
def solve1(): # Pass
    N = int(input())
    values = list(map(int, input().split()))
    dp=[1]*(N) # dp[i] : i번째 index에서의 최장 증가 부분 수열(LIS)
    
    for i in range(1,N):
        for j in range(i):
            if values[i] > values[j]:
                dp[i] = max(dp[i],dp[j]+1)
    print(max(dp))
    
# 완전 탐색
def solve2(): # 정답으로 보이나 O(2^N)으로 시간 초과
    global N, values
    N = int(input())
    values = list(map(int, input().split()))
    print(LIS(values))
    
def LIS(arry):
    if not arry: return 0
    
    ret = 1 # ret : return값
    for i in range(len(arry)): # arry[i] : LIS의 첫 수
        next = [] # LIS를 이루는 arry[i] 뒤에 이어질 후보값들
        for j in range(i,len(arry)):
            if arry[i] < arry[j]:
                next.append(arry[j]) 
        ret = max(ret, LIS(next)+1)
    return ret

# 이진탐색
def solve3():


if __name__== "__main__":
    solve1() #Pass
    solve2() #시간초과
    solve3() #