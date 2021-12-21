# https://www.acmicpc.net/problem/1085

# 문제 : 한 수 (x,y)가 주어졌을 때, 왼쪽 꼭지점(0,0) 및 오른쪽 꼭지점(w,h)을 지나가는 직사각형 거리 최솟값
# input : x y w h
# constraint : (0,0) - 좌측 꼭지점, (w,h) - 우측 꼭지점

import sys

def solve():
    input = sys.stdin.readline
    x,y,w,h = map(int,input().split())
    
    if x < w-x:
        dis_x = x
    else:
        dis_x = w-x
        
    if y < h-y:
        dis_y = y
    else:
        dis_y = h-y
        
    if dis_x > dis_y:
        print(dis_y)
    else:
        print(dis_x)

if __name__ == '__main__':
    solve()