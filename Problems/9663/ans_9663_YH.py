#https://www.acmicpc.net/problem/9663

import sys
# 파이썬으로 백트래킹 구현이 쉽지 않고, NQueen 문제에 적합하지 않은 언어라고 한다.
# Python3로는 시간 초과 / PyPy3로는 통과
# PyPy3는 메모리를 더 써서 자주 쓰이는 코드를 캐싱해서 실행속도 개선함. 
# 특이사항 : Q 초기화를 None으로 하면 시간초과 발생 / 0으로 하면 통과 - 이유는??
def PromisingCheck(row):
    for i in range(row):
        if (Q[i] == Q[row]) or ((row-i) == abs(Q[row]-Q[i])):
            return False
    return True

def NQueen(row):
    global cnt, N
    if row == N:
        cnt+=1
        return

    for col in range(N):
        Q[row] = col
        if PromisingCheck(row):
            NQueen(row+1)

def solve():
    input = sys.stdin.readline
    global N, Q, cnt
    N = int(input())
    Q = [0]*N
    cnt = 0
    NQueen(0)
    print(cnt)
    return
    
if __name__=="__main__":
    solve()
