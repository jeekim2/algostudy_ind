# https://www.acmicpc.net/problem/1931
# 문제 : N개의 회의에 대한 회의실 사용표 작성
# 입력 : 첫째 줄 - 회의 수 N, 둘째 줄 - N+1줄까지 각회의의 정보 (시작시간, 종료시간)
# 출력 : 회의의 최대 개수 출력

import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    meeting = []
    cnt = 1
    
    for _ in range(N):
        meeting.append(list(map(int,input().split())))

    meeting.sort(key=lambda x:(x[1],x[0]))
    print(meeting)
    
    for i in range(N):
        if i == 0:
            meeting_end = meeting[0][1]
        elif meeting_end <= meeting[i][0]:
            meeting_end = meeting[i][1]
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    solve()