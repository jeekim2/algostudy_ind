'''
https://www.acmicpc.net/problem/10871


'''
import sys

def findNum(TC, Th):
    if TC<Th:
        print(TC, end=' ')

def solve():
    input = sys.stdin.readline
    N, Max = map(int, input().split())
    TC_list = list(map(int,input().split()))

    for i in TC_list:
        findNum(i, Max)
    
if __name__ == "__main__":
    solve()