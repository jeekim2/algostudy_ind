'''
https://www.acmicpc.net/problem/1037
'''
import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int,input().split()))
    min = 1000000
    max = 0
    for i in A:
        if i<min:
            min = i
        if i>max:
            max = i
    print(min*max)

if __name__ == "__main__":
    solve()