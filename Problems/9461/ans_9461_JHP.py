# https://www.acmicpc.net/problem/9461
# 문제 : 파도반 수열

import sys

def padovan(x):
    global memo
    if memo.get(x):
        return memo[x]
    memo[x] = padovan(x-1) + padovan(x-5)
    return memo[x]

def solve():
    input = sys.stdin.readline
    global memo    
    N = int(input())
    TCs = []
    memo = {}
    
    for _ in range(N):
        TCs.append(int(input()))
    
    memo[1] = 1
    memo[2] = 1
    memo[3] = 1
    memo[4] = 2
    memo[5] = 2
    
    for val in TCs:
        print(padovan(val))

if __name__ == "__main__":
    solve()