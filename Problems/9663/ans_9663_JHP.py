# https://www.acmicpc.net/problem/9663
# 문제 : N-Queen 문제 - NxN인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램 작성

# ------------------------------------------------------
# 접근 방식 :
# (1) 기본 가정 - 같은 행 또는 대각선에 퀸을 놓지 않음
# 같은 행 : row[index] == row[i] 이면 tkddnl 노드 확인
# 대각선 : abs(row[index]-row[i] == index-i)

def queen(index):
    global row
    
    for i in range(index):
        if row[index] == row[i] or abs(row[index]-row[i]) == (index-i):
            return False
    return True

def dfs(index,N):
    global cnt
    global row
    
    if index == N: # 퀸의 갯수가 N개에 도달하여 완료된다면 cnt 증가 (조건 만족)
        cnt += 1
    else:          # 퀸의 갯수가 N개에 도달하지 못하면, dfs로 계속해서 겹치는 조건 확인
        for i in range(N):
            row[index] = i
            if queen(index): # 유망한 노드 확인 : 대각선/같은 행 위치 여부 확인 (Ture일 경우만)
                dfs(index+1,N)

def solve():
    global cnt
    global row
    
    N = int(input())
    cnt = 0
    row = [0]*N
    
    dfs(0,N)
    print(cnt)

if __name__ == '__main__':
    solve()