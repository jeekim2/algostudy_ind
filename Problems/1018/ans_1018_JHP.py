# https://www.acmicpc.net/problem/1018
# 문제 : 8x8짜리 체스판으로 잘라낸 후에 칠해야하는 최소의 정사각형 갯수

import sys

def solve():
    input = sys.stdin.readline
    N, M = map(int,input().split())
    board = []
    result = []
    
    for _ in range(N):
        board.append(input())
    
    # 브루트포스 풀기
    for i in range(N-7): # 8x8로 자르기 위해 i-7, j-7만큼 고정 필요 (끝에서 7번째)
        for j in range(M-7): # 상동 이유
            first_W = 0
            first_B = 0
            for k in range(i,i+8): # k~k+8까지 색칠하는 횟수 카운트
                for v in range(j,j+8):
                    if (k+v)%2 == 0: # 짝수 칸에 대한 처리 - 한칸씩 띄어가며 확인
                        if board[k][v] != 'W': # 짝수 칸이 W라고 가정한 경우
                            first_W += 1
                        else: # 짝수 칸이 B라고 가정한 경우
                            first_B += 1 
                    else: # 홀수 칸에 대한 처리 (위에 조건과 반대로 색칠 필요)
                        if board[k][v] != 'B': # 홀수 칸이 B라고 가정한 경우
                            first_W += 1
                        else: # 홀수 칸이 W라고 가정한 경우
                            first_B += 1      
            result.append(first_B)
            result.append(first_W)
    print(min(result))
        
if __name__ == '__main__':
    solve()