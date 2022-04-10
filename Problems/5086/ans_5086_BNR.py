'''
https://www.acmicpc.net/problem/5086
'''
import sys

def check(num1, num2):
    if num2%num1==0:
        return print('factor')
    elif num1%num2==0:
        return print('multiple')
    else:
        return print('neither')

def solve():
    input = sys.stdin.readline
    First = -1
    Second = -1

    while First and Second != 0:
        First, Second = map(int, input().split())
        if First == 0 and Second == 0:
            break
        else: 
            check(First, Second)

if __name__ == "__main__":
    solve()