# https://www.acmicpc.net/problem/2164
# 문제 : N개의 카드 중 마지막에 남는 카드의 숫자 찾기
# 입력 : N개의 카드 숫자
# 출력 : 마지막에 남는 카드 찾기

import sys

''' 시간 초과 
def solve_failed():
    input = sys.stdin.readline
    N = int(input())
    queue = []
    
    for i in range(1,N+1):
        queue.append(i)
    
    while len(queue) > 1:
        queue.remove(queue[0])
        temp = queue[0]
        queue.append(temp)
        queue.remove(queue[0])
    print(queue[-1])
'''
from collections import deque

def solve():
    input = sys.stdin.readline
    N = int(input())
    queue = deque()

    for i in range(1, N + 1):
        queue.append(i)

    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    print(queue[-1])

if __name__ == '__main__':
    solve()