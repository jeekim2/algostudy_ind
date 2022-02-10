'''
https://www.acmicpc.net/problem/12865

기본적인 0-1 배낭 문제(냅색)
https://chanhuiseok.github.io/posts/improve-6/
https://gsmesie692.tistory.com/113
'''

import sys

def knapsack(weight_value,num,max_w):
    dp = [[0]*(max_w+1) for _ in range(num+1)]    #dp[num][w] num번째까지 봤을 때 w무게까지의 최대 가치
    weight_value.insert(0,[0,0])    #인덱스 맞춰주려고
    for i in range (1,num+1):
        for w in range (1,max_w+1):
            # if i==0 or w==0:
            #     dp[i][w]= 0
            if weight_value[i][0]>w:  #i번쨰 무게가 w보다 크면 안넣어
                dp[i][w]=dp[i-1][w]
            else:   #물건을 안넣던가 공간확보하고 가치 더한 것 중 큰거
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight_value[i][0]]+weight_value[i][1])
                
            # print (dp)
    return dp[num][max_w]

def solve():
    N, K = map(int, sys.stdin.readline().split())
    W_V = [0]*N
    W_V = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
    
    print(knapsack(W_V,N,K))
    

if __name__ == "__main__":
    solve()