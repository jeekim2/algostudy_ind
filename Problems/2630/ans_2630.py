import sys
input = sys.stdin.readline
N = int(input())
paper = []
result = []
for i in range(N):
    paper.append(list(map(int, input().split()))) #int 자료형
    

def solution(x, y, N):
  num = paper[x][y]   # 변수에 각 정사각형 종이의 자리 할당 
  for i in range(x, x+N):  # 시작점과 숫자가 같은지 반복문을 돌면서 확인
    for j in range(y, y+N):
      if num != paper[i][j]:  # 숫자가 다르면 4분할
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if num == 0:
    result.append(0)
  else: 
    result.append(1)


solution(0,0,N)
print(result.count(0))  # 흰종이
print(result.count(1))  # 파랑종이