#https://www.acmicpc.net/problem/17386
#CCW 반시계 방향 1, 시계방향 -1, 일직선 0, #11758문제 참고
#(1)두 선분 일직선, 겹치거나 겹치지 않거나, CCW 0
#(2)A,B 선분과  C,D 선분이 교차한다고 했을 때, CCW(A,B,C)*CCW(A,B,D) = -1
#(3)A,B 선분과  C,D 선분이 교차하지 않을 때, CCW(A,B,C)*CCW(A,B,D) = 1
#이 문제는 3점이 일직선인 경우가 없음
import sys
input = sys.stdin.readline


def CCW( x1, y1, x2, y2, x3, y3):
    k = (y3-y1)*(x2-x1)-(y2-y1)*(x3-x1)

    if k>0:
        return  1
    elif k<0:
        return -1
    else:
        return 0

def solve():
    x1, y1, x2, y2 = list(map(int,input().split()))
    x3, y3, x4, y4 = list(map(int,input().split()))

    ans1 = CCW( x1, y1, x2, y2, x3, y3)*CCW( x1, y1, x2, y2, x4, y4)
    ans2 = CCW( x3, y3, x4, y4, x1, y1)*CCW( x3, y3, x4, y4, x2, y2)

    if ans1<0 and ans2<0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    solve()