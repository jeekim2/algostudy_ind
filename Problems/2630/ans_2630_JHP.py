# https://www.acmicpc.net/problem/2630
# 문제 : 정사각형 모양의 같은 색(0,1) 종이를 나누는 문제
# 입력 : 첫째줄 = N, NxN의 정사각형
# 출력 : 첫째 줄 = 하얀색 색종이, 둘째 줄 = 파란색 종이

import sys

def paper_div(x,y,n):
    global one,zero
    global array_n    
    check=array_n[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=array_n[i][j]:     #나머지 사각형의 색깔과 일치하지 않는다면 실행합니다.
                paper_div(x,y,n//2)            #1사분면
                paper_div(x,y+n//2,n//2)       #2사분면
                paper_div(x+n//2,y,n//2)       #3사분면
                paper_div(x+n//2,y+n//2,n//2)  #4사분면
                return

    if check==0:
        zero+=1
        return
    else:
        one+=1
        return

def solve():
    global one,zero
    global array_n  
    input = sys.stdin.readline
    N = int(input())
    array_n = []
    one, zero = 0,0
    for i in range(N):
        array_n.append(list(map(int, input().split())))
    
    paper_div(0,0,N)
    
    print(zero)
    print(one)

if __name__ == "__main__":
    solve()