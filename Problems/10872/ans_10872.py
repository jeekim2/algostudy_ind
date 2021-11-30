# https://www.acmicpc.net/problem/10872
# 문제 : Factorial 재귀함수 사용

import sys

def factor(num):
    if num <= 1:
        return 1
    else:
        return num * factor(num-1)

def solve():
    input = sys.stdin.readline
    N = int(input())
    
    result = factor(N)
    print(result)   

if __name__ == "__main__":
    solve()