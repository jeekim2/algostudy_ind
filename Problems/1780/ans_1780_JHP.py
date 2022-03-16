# https://www.acmicpc.net/problem/1780
# 문제 : -1,0,1로만 구성된 종이의 숫자 갯수 출력
# 입력 : 첫째줄 - N, 둘째줄 - N x N에 들어가는 array 숫자
# 출력 : -1만 있는 숫자, 0만 있는 숫자, 1만 있는 숫자

import sys

def paper_num(x_pos,y_pos,n):
    global array_input
    global result
    
    check = array_input[x_pos][y_pos]
    flg = False
    for i in range(x_pos,x_pos+n):
        for j in range(y_pos,y_pos+n):
            if check != array_input[i][j]:
                n = n//3
                for x in range(3):
                    for y in range(3):
                        paper_num(x_pos+x*(n),y_pos+y*(n),n)
                return
    
    if check == -1:
        result[0] += 1
    elif check == 0:
        result[1] += 1
    else:
        result[2] += 1

def solve():
    global array_input
    global result
    
    input = sys.stdin.readline
    N = int(input())
    array_input = []
    result = [0,0,0]
    for _ in range(N):
        array_input.append(list(map(int,input().split())))
        
    paper_num(0,0,N)

    for val in result:
        print(val)

if __name__ == '__main__':
    solve()