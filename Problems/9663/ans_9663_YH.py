#https://www.acmicpc.net/problem/9663

import sys
# 시간초과 발생
# 파이썬으로 백트래킹 구현이 쉽지 않고, NQueen 문제에 적합하지 않은 언어라고 한다.
# 최적화에 대해서 다시 고민해봐야겠다.
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
