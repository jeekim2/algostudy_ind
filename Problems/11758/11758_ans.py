#https://www.acmicpc.net/problem/11758

import sys

input = sys.stdin.readline

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

k = (y3-y1)*(x2-x1)-(y2-y1)*(x3-x1)

if k == 0:
    print(0)
elif k<0:
    print(-1)
else:
    print(1)