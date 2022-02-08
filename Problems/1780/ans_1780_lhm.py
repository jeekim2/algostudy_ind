#https://www.acmicpc.net/problem/1780
import sys

input = sys.stdin.readline

N = int(input())
temp = []

minus = 0
zero  = 0
plus = 0

for i in range(N):
  temp.append(list(map(int, input().split())))



def func(x,y,k):
  global minus, zero, plus
  num = temp[x][y]

  for i in range(x, x+k):
    for j in range(y, y+k):
      if num!= temp[i][j]:
        for a in range(3):
          for b in range(3):
            func(x+a*k//3,y+b*k//3,k//3)
        return
  
  if num == -1:
    minus = minus + 1
  elif num == 0:
    zero = zero + 1
  else:
    plus = plus + 1



func(0,0,N)

print(minus)
print(zero)
print(plus)