# https://www.acmicpc.net/problem/1629
# 문제 : 자연수 A를 B번 곱한 수를 C로 나눈 나머지를 구하기
# 입력 : 자연수 A,B,C (2,137,483,647 이하)
# 출력 : 첫번째 줄에 A를 B번 곱한 수를 C로 나눈 나머지 출력

import sys

def multi(A,B,C):
    if B == 1:
        val = A%C
        return val
    
    val = multi(A,B//2,C) # B//2만큼 분할하여 계산
    
    if B%2 == 1:
        val = (val*val*A)%C
        return val
    else:
        val = (val*val)%C
        return val

def solve():
    input = sys.stdin.readline
    A,B,C = list(map(int,input().split()))
    result = multi(A,B,C)
    print(result)

if __name__ == '__main__':
    solve()