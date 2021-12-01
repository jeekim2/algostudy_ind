# https://www.acmicpc.net/problem/11050

# 문제 : 이항계수 N/K를 구하는 프로그램 작성
# 이항 계수란? N! / (N-K)! K!

# 아래 For를 이용하면 Run time Error 발생
# 따라서, 재귀함수의 활용하는 것으로 Runtime Error를 방지할 필요가 있음. (재귀로 다시 풀어보자)

import sys

def recursive(num):
    if num <= 1: # num-1이 0,1이 되었을 시 처리 필요
        return 1
    else:
        return num*recursive(num-1)        

def solve():
    N, K = list(map(int,input().split()))
    # N, K = map(int, sys.stdin.readline().strip().split()) # 이렇게도 가능

    result = recursive(N)/(recursive(N-K) * recursive(K))
    print("{:.0f}".format(result), sep='') # "{:.(소숫점)f}".format(num)

if __name__ == "__main__":
    solve()