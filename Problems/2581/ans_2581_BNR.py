# https://www.acmicpc.net/problem/2581
# 문제 : 자연수 M이상 N이하에 존재한 소수의 합과 최솟값을 찾는 프로그램 작성
# input : M, N

M = int(input()) #M 이상
N = int(input()) #N 이하

sum = 0
min = 0

if N <= 2:
    if N == 2:
        sum = 2
        min = 2

else:
    for i in range(N,M-1,-1):
        n = 2
        if i == 1:
            cnt = cnt
        elif i == 2:
            cnt = cnt + 1
        else:
            while n < i:
                if i % n == 0:
                    # n = n +1
                    break
                if n == i - 1:
                    sum = sum +i
                    min = i
                n = n + 1

if sum==0 and min == 0:
    print('-1')
else:
    print(sum)
    print(min)
