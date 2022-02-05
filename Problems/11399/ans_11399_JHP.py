# https://www.acmicpc.net/problem/11399
# 문제 : ATM 1대에서 뽑을 수 있는 최소 시간 구하기
# 입력 : 첫째줄 - 사람 숫자 N, 둘째줄 - 각 사람마다 걸리는 시간
# 출력 : 최소 시간 출력

import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    atm = list(map(int,input().split()))
    time = []
    temp_time = 0
    
    atm.sort()
    
    for val in atm:
        temp_time += val
        time.append(temp_time)
    print(sum(time))

if __name__ == '__main__':
    solve()