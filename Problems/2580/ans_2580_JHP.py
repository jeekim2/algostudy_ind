# https://www.acmicpc.net/problem/2580
# 문제 : 9x9 스도쿠 문제 풀기
# 제한 : PyPy3 1172ms 이하

# 접근방법 : DFS(깊이 우선 탐색) 및 백트래킹(브루트 포스) 사용
# 제한 조건이 있으므로, 유망한 숫자 검사와 재귀를 최소화 해야함.

import sys

def isCorrect(x,y): # 유망한 숫자 검사 조건
    global board
    global nums
    
    for i in range(0,9):
        # (1) 가로, 세로 줄에 동일 숫자가 있으면 안됨
        if board[x][y] == board[i][y]:
            nums.remove(board[x][i])
        if board[x][y] == board[x][i]:
            nums.remove(board[i][y])
        
        # (2) 3x3 내 숫자 찾기
        x //= 3
        y //= 3
        for j in range(x*3,(x+1)*3):
            for k in range(y*3,(y+1)*3):
                if board[j][k] in nums:
                    nums.remove(board[j][k])
        return nums
                
def findNum(x,y):
    global board
    global check
    
    if check == True:
        return
    if x == 9:  # row 완료 이후
        for row in board:
            print(*row)
        check = True
        return check
    else:
        result = isCorrect(x,y)
        for val in result:
            board[x][y] = val
            findNum(x+1,0)
            board[x][y] = 0

def solve():
    global board
    global nums
    global check
    
    input = sys.stdin.readline
    board = []
    nums  = [1,2,3,4,5,6,7,8,9]
    check = [False]
    
    for i in range(9):
        board.append(list(map(int,input().split())))
    findNum(0,0)

if __name__ == "__main__":
    solve()