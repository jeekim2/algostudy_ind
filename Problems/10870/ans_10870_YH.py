#https://www.acmicpc.net/problem/10870

import sys

def fibonacci(n):
    if n<=1:
        return n
    result = fibonacci(n-1)+fibonacci(n-2)
    return result

def solve():
    input = sys.stdin.readline
    n = int(input())
    result = fibonacci(n)
    print(result)
    
if __name__=="__main__":
    solve()