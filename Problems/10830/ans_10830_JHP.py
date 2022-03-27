# https://www.acmicpc.net/problem/10830
# 문제 : NxN크기의 행렬 A과 정수 B가 주어졌을 때, 행렬의 B 제곱 구하기
# 입력 : 첫째줄 = 행렬크기 N과 B, 둘째줄부터 N개의 줄까지 = 행렬 A의 원소 N개, 
# 출력 : N개의 줄에 행렬 A를 B만큼 제곱을 1000으로 나눈 행렬값 출력

import sys

def power(A,B,N):
    result = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(N):
                temp += B[i][k] * A[k][j]
            result[i][j] = temp%1000
    return result

def solve():
    input = sys.stdin.readline
    N, B = map(int,input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int,input().split())))    

    # 아래처럼 for를 이용하면 시간초과 발생
    # ans = A
    # for i in range(B-1):
    #     if B == 1:
    #         ans = A
    #     else:
    #         ans = power(A,ans,N)

    # 따라서 분할 정복 전략 필요
    ans = [[0]*N for _ in range(N)]
    for i in range(N):
        ans[i][i] = 1 # unit matrix
    while B:
        if B&1: # B가 홀수일 때마다 연산
            ans = power(A,ans,N)
        A = power(A,A,N)
        B //= 2

    for val in ans:
        print(*val)        

if __name__ == "__main__":
    solve() 