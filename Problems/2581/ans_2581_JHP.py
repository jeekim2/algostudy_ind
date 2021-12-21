# https://www.acmicpc.net/problem/2581
# 문제 : 자연수 M이상 N이하에 존재한 소수의 합과 최솟값을 찾는 프로그램 작성
# input : M, N
# version 1 : remove()사용시, 메모리(29452KB) & Time (504ms)

import sys

def solve():
    input = sys.stdin.readline
    M = int(input())
    N = int(input())
    num = []
    num2 = []
    
    for i in range(M,N+1):
        num.append(i)
        num2.append(i)
    
    for val in num:
        if val >= 2:
            for j in range(2,val):
                if val % j == 0:
                    num2.remove(val)
                    break
        else:
            num2.remove(val) # 0,1의 경우, 소수가 아니기 때문에 else 처리 필요
            
    if len(num2) > 0:
        print(sum(num2))
        print(min(num2))
    else:
        print(-1)    
    

if __name__ == '__main__':
    solve()

