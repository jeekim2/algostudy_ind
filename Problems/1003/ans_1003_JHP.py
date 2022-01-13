# https://www.acmicpc.net/problem/1003
# (Solve)Dynamic programming의 경우 : 76ms
# (Solve2)Non-Dynamic programming의 경우 : 시간 초과

# method(1) - 동적 계획법으로 재귀 횟수 줄이기
def fibonacci(x):
    if x == 0:
        return dp_num[0]
    elif x == 1:
        return dp_num[1]
    else:
        if x == 2: # DP 여부 확인 목적
            print(200)
        for i in range(2, x+1):
            dp_num[i] = [dp_num[i-1][0]+dp_num[i-2][0], dp_num[i-1][1]+dp_num[i-2][1]]
        return dp_num[i]

# method(2) - 재귀로 문제 풀기
def fibonacci_not_DP(x):
    global cnt_0, cnt_1
    
    if x == 0:
        cnt_0 += 1
        return 0
    elif x == 1:
        cnt_1 += 1
        return 1
    else:
        return fibonacci_not_DP(x-1) + fibonacci_not_DP(x-2)

def solve():
    global dp_num

    result = dict()
    dp_num = dict()    
    dp_num[0] = [1,0] # zero가 나오는 table 값
    dp_num[1] = [0,1] # one이 나오는 table 값
    
    test_n = int(input())
    
    for i in range(test_n):
        N = int(input())
        result[i]=fibonacci(N)
    
    for j in range(test_n):
        print(*result[j])

# non-Dynamic programming
def solve2():
    global cnt_0, cnt_1
    global result_not_dp
    result_not_dp = []
    
    test_n = int(input())
    
    for i in range(test_n):
        N = int(input())
        cnt_0 = 0
        cnt_1 = 0
        fibonacci_not_DP(N)
        result_not_dp.append([cnt_0,cnt_1])
    for j in range(test_n):
        print(*result_not_dp[j])

if __name__ == "__main__":
    solve()  # Dynamic Programming 해결 
    solve2() # non-Dynamic Programming 해결
