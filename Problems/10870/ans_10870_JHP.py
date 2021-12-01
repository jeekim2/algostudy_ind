# https://www.acmicpc.net/problem/10870
# 문제 : 피보나치 수
# 피보나치 수 : F(n) = F(n-1)+F(n-2) (n>=2)

import sys

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)    

def solve():
    
    input = sys.stdin.readline
    num = int(input())
    num_list = []
    
    for i in range(num+1):
        num_list.append(fibo(i))
    print(num_list)
    result = num_list[num]
    print(result)

if __name__ == "__main__":
    solve()