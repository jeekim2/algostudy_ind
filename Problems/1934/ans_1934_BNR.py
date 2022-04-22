# https://www.acmicpc.net/problem/1934

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    for _ in range(N):
        a,b= map(int,input().split())
        A,B = a,b
        
        while B != 0:
            A = A%B
            A,B = B,A
        print(a*b//A)


if __name__ == "__main__":
    solve()