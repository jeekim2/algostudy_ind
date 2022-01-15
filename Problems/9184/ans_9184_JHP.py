# https://www.acmicpc.net/problem/9184
# 문제 : 재귀함수 w(a,b,c)

import sys

# 재귀함수
def w_to(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w_to(20,20,20)
    elif a < b and b < c:
        return w_to(a,b,c-1) + w_to(a,b-1,c-1) - w_to(a,b-1,c)
    else:
        w_to(a-1,b,c) + w_to(a-1,b-1,c) + w_to(a-1,b,c-1) - w_to(a-1,b-1,c-1)

# DP 해결 - memoization
def w(a,b,c):
    global w_mem
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        w_mem[(20, 20, 20)] = w(20,20,20)
        return w_mem[(20, 20, 20)]
    elif a < b and b < c:
        w_mem[(a,b,c)] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return w_mem[(a,b,c)]
    else:
        w_mem[(a,b,c)] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return w_mem[(a,b,c)]

def solve():
    global w_mem
    
    input = sys.stdin.readline
    w_mem = dict() # memoization을 위한 dict 설정
    temp_input = []

    while True:
        a,b,c = list(map(int,input().split()))
        if a == b == c == -1:
            break
        else:
            temp_input.append([a,b,c])
            
    for val in temp_input:
        a,b,c = val
        print(f'w({a},{b},{c}) = {w(a,b,c)}')

if __name__ == '__main__':
    solve()