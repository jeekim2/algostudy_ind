'''
https://www.acmicpc.net/problem/11047

K원을 만드는데 필요한 동전 개수 최솟값
'''
import sys


def findcoin(N,K):
    cnt = 0
    tmp = 0
    for i in range(N-1,-1,-1):
        if coin[i]>K:
            continue
        tmp = K//coin[i]
        cnt = cnt + tmp
        K = K - tmp*coin[i]
    return cnt

def solve():
    N,K = map(int, sys.stdin.readline().split())
    global coin
    coin = []
    for _ in range(N):
        coin.append(int(sys.stdin.readline()))
    
    print(findcoin(N,K))

if __name__ == "__main__":
    solve()