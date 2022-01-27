'''
https://www.acmicpc.net/problem/2579

크기 N개인 삼각형의 선택된 수의 합이 최대
'''
import sys

N = int(input())
dp = [0]*N  #dp 메모리

stair = [int(sys.stdin.readline()) for _ in range(N)] #input

if N==1:
    dp[0] = stair[0]
    print(dp[N-1])
elif N==2:
    dp[1] = max(stair[0]+stair[1], stair[1])
    print(dp[N-1])
elif N==3:
    dp[2] = max(stair[1]+stair[2], stair[0]+stair[2])
    print(dp[N-1])
else:
    dp[0] = stair[0]
    dp[1] = max(stair[0]+stair[1], stair[1])
    dp[2] = max(stair[1]+stair[2], stair[0]+stair[2])
    for i in range(3,N):
        # dp[i] = dp[i-2]+stair[i]    #이전 계단을 밟지 않은 경우
        # dp[i] = dp[i-3]+stair[i-1]+stair[i]    #이전 계단을 밟은 경우
        dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])
    print(dp[-1])
