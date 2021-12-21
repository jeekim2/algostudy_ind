# https://www.acmicpc.net/problem/7568
# 문제 : (x,y) = (kg,cm)로 표현된다고 할때, 덩치가 큰 순위를 판단
# 판단 기준 : x1 > x2, y1 > y2 ==> (x1,y1)이 덩치가 더 큼

# 입력 : 전체 사람의 수 N, N개의 줄에 각 사람의 몸무게 및 키
# 출력 : 나열된 인원의 덩치 등수

import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    person = []
    
    for i in range(N):
        x, y = list(map(int,input().split()))
        person.append([x,y])
    
    for i in person:
        score = 1
        for j in person:
            if i[0] < j[0] and i[1] < j[1]:
                score += 1
        print(score, end="")

if __name__ == '__main__':
    solve()