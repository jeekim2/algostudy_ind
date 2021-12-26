#https://www.acmicpc.net/problem/14888

import sys

#백트래킹 방식에 대한 생각 틀을 정립해봐야겠다....
def solve():
    input = sys.stdin.readline
    n = int(input())
    Operand = list(map(int,input().split()))
    Operator = list(map(int,input().split()))
