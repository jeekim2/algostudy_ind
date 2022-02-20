#https://www.acmicpc.net/problem/1934
import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    a, b = map(int, input().split())

    c, d = a, b
    q, r = 0, 0 #q = 몫, r = 나머지
    
    while True: #유클리드 호제법
        if a < b:
            a,b = b,a
        
        q = a//b
        r = a - b*q

        if r == 0:
            gcd = b # 최대 공약수
            break
        a = b
        b = r
    print(c*d//gcd) #최초 두 숫자의 곱에 최대 공약수로 나누기


