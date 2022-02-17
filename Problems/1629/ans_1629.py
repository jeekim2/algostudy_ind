#https://www.acmicpc.net/problem/1629
# (A^B)%C 로 하게 되면 시간 복잡도가 올라가서 분할로 접근해야 함

A, B, C = list(map(int, input().split()))

def func(a, b, c):
  if b == 1:
    return a % c

  n = func(a, b//2, c)
  if b%2 :
    return (n*n*a)%c 
  else:
    return (n*n)%c


print(func(A,B,C))