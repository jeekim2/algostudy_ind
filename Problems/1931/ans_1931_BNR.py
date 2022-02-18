'''
https://www.acmicpc.net/problem/1931

회의 최대 가능 수
'''
import sys

def meeting_1(list,num):  #시간초과 발생
    cnt = 1
    i = 0
    while i<num:
        end = list[i][1]
        for j in range(i+1,num):
            nextstart = list[j][0]
            if nextstart<end:
                if j == num-1:
                    i+=1
                    break
                else:
                    continue
            else:
                cnt+=1
                i = j
                break
        if i == num-1:
            return cnt

def solve1():  #시간초과
    N = int(sys.stdin.readline())
    meeting_list = []*N
    meeting_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] #[시작시간,종료시간]
    meeting_list.sort()

    dp = [0]*(N+1) 
    for i in range(1,N+1):
        dp[i] = max(dp[i-1],meeting_1(meeting_list[i-1:], N+1-i)) #정렬된 리스트에서 앞부터 회의 최댓값 계산
    print(dp[N])

def meeting_2(list,num):
    cnt = 1
    for i in range(num):
        if i == 0:
            end = list[0][1]
        elif end <= list[i][0]:
            end = list[i][1]
            cnt += 1
    return cnt

def solve2():  
    N = int(sys.stdin.readline())
    meeting_list = []*N
    meeting_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] #[시작시간,종료시간]
    meeting_list.sort(key=lambda x:(x[1],x[0]))
    print(meeting_2(meeting_list, N))

if __name__ == "__main__":
    # solve1()
    solve2()
