'''
https://www.acmicpc.net/problem/2164

디큐 (deque)
시간 복잡도 (1)
양 방향에서 삭제, 삽입 가능한 자료 구조

'''
import sys
from collections import deque

def solve_deque():
    N = int(sys.stdin.readline())
    Q_list = deque(i for i in range (1,N+1))
    # print(Q_list)

    while len(Q_list)>1:
        Q_list.popleft()
        Q_list.append(Q_list.popleft())
    print(Q_list[0])

if __name__ == "__main__":
    solve_deque()