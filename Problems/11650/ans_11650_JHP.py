# https://www.acmicpc.net/problem/11650
# 문제 : x 좌표 기준으로 정렬, x 좌표가 같다면 y 기준 정렬
# 결과(1) : 메모리(49708KB),시간(444ms) / 결과(2) : 메모리(56888KB),시간(404ms)

import sys

def solve():
    input = sys.stdin.readline
    num = int(input())
    points = []
    for _ in range(num):   
        points.append(list(map(int,input().split())))
        
    # (1) Sort 사용하기
    s_points = sorted(points)
    for i in range(num):
        print(s_points[i][0],s_points[i][1])    
    
    # (2) key 값으로 정렬하기 : sort method에 key를 주면 sort 가능
    points.sort(key=lambda x: (x[0],x[1])) # x[0] 및 x[1] 오름차순 정렬
    for i in range(num):
        print(points[i][0],points[i][1])    
    
if __name__ == '__main__':
    solve()