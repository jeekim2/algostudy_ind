#https://www.acmicpc.net/problem/9663

import sys
# 시간초과 발생
def PromisingCheck(row):
    
    for i in range(row):
        if (Q[i] == Q[row]) or ((row-i) == abs(Q[row]-Q[i])):
            return False
    return True

def NQueen(row):
    global cnt, cc
    cc+=1
    if row == N:
        cnt+=1
        return
    for col in range(N):
        Q[row] = col
        if PromisingCheck(row):
            NQueen(row+1)
            
def solve():
    input = sys.stdin.readline
    global N, Q, cnt,cc
    N = int(input())
    Q = [None]*N
    cnt = 0
    cc = 0
    NQueen(0)
    print(cnt)
    print(cc)
    
if __name__=="__main__":
    solve()