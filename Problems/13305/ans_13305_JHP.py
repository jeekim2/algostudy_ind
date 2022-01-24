# https://www.acmicpc.net/problem/13305
# 문제 : 준규가 가지고 있는 동전 N 종류 동전, 동전의 합 = K 가치를 만들 때 최소 동전 갯수
# 입력 : 첫째 줄 = N, K 둘째 줄 = N개의 줄에 동전의 가치 (오름차순)
# 출력 : 첫째 줄에 K원을 만드는데 필요한 최소 동전 개수
# -------------------------------------------
# 그리디 알고리즘 (탐욕법)

import sys

def solve():
    coin = []
    sum = 0
    cnt = 0
    
    input = sys.stdin.readline
    N,K = list(map(int,input().split()))
    
    for _ in range(N):
        coin.append(int(input()))
    coin.sort()

    while sum != K:
        if len(coin) == 0 :
            break
        else:
            if K//coin[-1] < 1:
                coin.pop()
            else:
                temp_cnt = (K-sum)//coin[-1]
                sum += coin[-1]*temp_cnt
                cnt += temp_cnt
                coin.pop()
    print(cnt)
    
if __name__ == '__main__':
    solve()