# https://www.acmicpc.net/problem/1992

import sys

def quadtree(x_pos,y_pos,num,input_arr):
    check = input_arr[y_pos][x_pos] 
    for i in range(x_pos, x_pos+num):
        for j in range(y_pos, y_pos+num):
            if check != input_arr[j][i]:
                check = '-'
                break
    
    if check == '-':
        print("(",end="")
        num = num//2
        quadtree(x_pos,y_pos,num,input_arr)
        quadtree(x_pos+num,y_pos,num,input_arr)
        quadtree(x_pos,y_pos+num,num,input_arr)
        quadtree(x_pos+num,y_pos+num,num,input_arr)
        print(")",end="")
    elif check == 1:
        print('1',end="")
    else:
        print('0',end="")
    

def solve():
    input = sys.stdin.readline
    N = int(input())
    input_arr = []
    
    for _ in range(N):
        input_arr.append(list(map(int,input().rstrip()))) # rstrip 기억

    quadtree(0, 0, N, input_arr)

if __name__ == "__main__":
    solve()