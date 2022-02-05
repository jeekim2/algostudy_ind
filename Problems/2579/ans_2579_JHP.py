# https://www.acmicpc.net/problem/2579
# 문제 : 아래 규칙에 따라 오르면서 계단을 올랐을 때, 최댓값을 구하기
# 조건(1) : 한번에 한 계단 또는 두 계단 오르기 가능
# 조건(2) : 연속된 세 개의 계단을 모두 밟을 수 없음. (단, 시작점은 미포함)
# 조건(3) : 마지막 도착 계단은 반드시 밟아야 함.
# 입력 : 첫째 줄에 계단 개수, 둘째 줄에 한줄에 하나씩 계단 점수 (1단부터)
# 출력 : 총 점수의 최댓값

def solve():
    N = int(input())
    temp_sum1 = 0
    temp_sum2 = 0
    
    stair = [0 for _ in range(N)]
    memo = [0 for _ in range(N)]
        
    for i in range(N):
        stair[i] = int(input())
    
    if N == 1:
        memo[0] = stair[0]
        print(memo[0])
        return
    if N == 2:
        memo[1] = stair[0] + stair[1]
        print(memo[1])
        return
    else:
        memo[0] = stair[0]
        memo[1] = stair[0] + stair[1]
        memo[2] = max(stair[1]+stair[2], stair[0]+stair[2])
        for i in range(3,N):
            temp_sum1 = memo[i-3]+stair[i-1]+stair[i]
            temp_sum2 = memo[i-2]+stair[i]        
            memo[i] = max(temp_sum1,temp_sum2)
        print(memo[-1])
        return

if __name__ == "__main__":
    solve()