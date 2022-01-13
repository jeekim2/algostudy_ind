#https://www.acmicpc.net/problem/14501


N = int(input())
T = [0]*N
P = [0]*N
dp = [0]*(N+1)
for i in range(N):
    T[i], P[i] = map(int, input().split()) #입력

for i in range(N-1,-1,-1):  # 뒤 부터 계산
    if T[i] + i > N:        # 상담 끝나는 시간이 N보다 클 때, 상담 안해
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i]+dp[i + T[i]])    #일안했을 때vs i의 일을 했을 때 값 비교

print(dp[0])
