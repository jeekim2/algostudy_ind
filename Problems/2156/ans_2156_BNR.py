'''
https://www.acmicpc.net/problem/2156

1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
'''
import sys

def wineselect(N, wine):
    # dp[i] = wine[i-1] + dp[i-3] + wine[i] #이전 잔 마셨을 경우
    # dp[i] = dp[i-2] + wine[i]   #이전 잔 안마실 경우
    # dp[i] = dp[i-1] #안마셔도 됨

    dp =[0]*N
    if N>=1:
        dp[0] = wine[0]

    if N>=2:
        dp[1] = wine[0] + wine[1]

    if N>=3:
        dp[2] = max(wine[0]+wine[1], wine[0]+wine[2], wine[1]+wine[2])

    if N>=4:
        for i in range(3,N):
            dp[i] = max(wine[i]+wine[i-1]+dp[i-3], wine[i]+dp[i-2], dp[i-1])

    return dp[-1]

def solve():
    N = int(input())
    wine = [int(sys.stdin.readline()) for _ in range(N)]
    print(wineselect(N, wine))

if __name__ == "__main__":
    solve()    