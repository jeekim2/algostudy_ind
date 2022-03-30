# https://www.acmicpc.net/problem/2740
# 문제 : M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램 작성
# 입력 : 첫째줄 = A의 크기 N과 M, 둘째줄부터 N개의 줄까지 = 행렬 A의 원소 M개, 
#       다음줄 = 행렬 B의 크기 M과 K, 다음줄부터 M개의 줄까지 = 행렬 B의 원소 K개
# 출력 : N개의 줄에 행렬 A와 B를 곱한 행렬 출력

import sys

def product(A,B,N,K,M):
    result = [[0]*K for _ in range(N)]

    for i in range(N):
        for j in range(K):
            temp = 0
            for k in range(M):
                temp += A[i][k] * B[k][j]
            result[i][j] = temp
    return result

def solve():
    input = sys.stdin.readline
    N, M = map(int,input().split())
    A = []
    B = []
    for _ in range(N):
        A.append(list(map(int,input().split())))
    
    M, K = map(int,input().split())
    for _ in range(M):
        B.append(list(map(int,input().split())))    
        
    ans = product(A,B,N,K,M)

    for val in ans:
        print(*val)        

if __name__ == "__main__":
    solve()