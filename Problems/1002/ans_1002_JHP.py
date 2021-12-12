# https://www.acmicpc.net/problem/1002
# 문제 : 조규현 (x1,y1) -> r1, 백승환 (x2,y2) -> r2 : 류재명이 있을 수 있는 좌표의 수 계산
# input : (1) T = test case, (2) x1,y1,r1, x2,y2,r2
# output :  각 테스트마다 류재명이 있을 수 있는 위치의 수 출력, 무한대일 경우 '-1' 출력

import sys

def solve():
    
    input = sys.stdin.readline
    T = int(input())
    
    for _ in range(T):
        x1,y1,r1,x2,y2,r2 = map(int,input().split())
        r = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
        
        if r == 0 and r1 == r2: # infinite case need to concern as seperate condition
            print('-1')
        else:
            point = sorted([r1,r2,r])
            r1 = point[0]
            r2 = point[1]
            r = point[2]

            if r > (r1+r2):
                print('0')
            elif r == (r1+r2) or r == abs(r1-r2):
                print('1')
            else:
                print('2')

if __name__ == "__main__":
    solve()