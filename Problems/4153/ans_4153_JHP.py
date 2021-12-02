# https://www.acmicpc.net/problem/4153
# 문제 : 파타고라스의 정의

import sys

def solve():
    
    while True:
        
        input = sys.stdin.readline
        x, y, z = map(int,input().split())
    
        if [x,y,z] == [0,0,0]:
            break
        else:
            point = [x,y,z]
            point.sort()

            x = point[0]
            y = point[1]
            z = point[2]
            
            if z*z == (x*x+y*y):
                print('right')
            else:
                print('wrong')

if __name__ == '__main__':
    solve()