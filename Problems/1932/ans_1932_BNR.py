'''
https://www.acmicpc.net/problem/1932

크기 N개인 삼각형의 선택된 수의 합이 최대
'''
import sys

N = int(input())
TA = []
dp = [[0]*i for i in range(1,N+1)]      #dp메모리 선언

# for _ in range(N):
#     TA.append(list(map(int, input().split())))
TA= [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp[0] = TA[0]

dp[1][0] = dp[0][0]+TA[1][0]
dp[1][1] = dp[0][0]+TA[1][1]

# dp[2][0] = dp[1][0]+TA[2][0]
# dp[2][1] = max(dp[1][0]+TA[2][1], dp[1][1]+TA[2][1])
# dp[2][2] = dp[1][1]+TA[2][2]

# dp[3][0] = dp[2][0]+TA[3][0]
# dp[3][1] = max(dp[2][0]+TA[3][1], dp[2][1]+TA[3][1])
# dp[3][2] = max(dp[2][1]+TA[3][2], dp[2][2]+TA[3][2])
# dp[3][3] = dp[2][2]+TA[3][3]

for i in range(2,N):
    dp[i][0] = dp[i-1][0]+TA[i][0]
    dp[i][i] = dp[i-1][i-1]+TA[i][i]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1]+TA[i][j], dp[i-1][j]+TA[i][j])

print(max(dp[-1]))