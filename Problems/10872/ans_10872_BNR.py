# https://www.acmicpc.net/problem/10872
# 문제 : Factorial 재귀함수 사용

N = int(input())

def Fac(num):
    if num>1:
        return num*(Fac(num-1))
    else:
        return 1
print(Fac(N))