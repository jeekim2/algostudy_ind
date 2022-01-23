# https://www.acmicpc.net/problem/1149
# 문제 : RGB 거리에 집 N개가 있음. 빨/초/파 중 색을 칠했을 때 최소 비용이 드는 조합 찾기
# 조건 (1). 1,2번 집의 색이 달라야함.
# 조건 (2). N번 집의 색이 N-1번 집의 색과 달라야 함.
# 조건 (3). i(2<=i<=N-1)번집의 색은 i-1번, i+1번 집과 달라야 함.
# -> 즉, 연속적으로 같은 색상을 사용할 수 없음.

# 입력 : 첫번째 줄 = N개의 집, 둘째 줄 = 빨/초/파 가격
# 출력 : 모든 집을 칠하는 비용의 최솟값 출력

def solve():
    N = int(input())
    
    home = [[0 for _ in range(3)] for __ in range(N)] # Array 사이즈 지정
    memo = [[0 for _ in range(3)] for __ in range(N)] # Array 사이즈 지정
    
    for i in range(N):
        red, green, blue = list(map(int,input().split()))
        home[i] = [red, green, blue]
    
    for j in range(N):
        if j == 0: # 첫번째 집
            memo[j][0] = home[j][0]
            memo[j][1] = home[j][1]
            memo[j][2] = home[j][2]
        else: # 싼 가격을 기준으로 다른 페인트를 더해가는 부분
            memo[j][0] = home[j][0] + min(memo[j-1][1], memo[j-1][2])
            memo[j][1] = home[j][1] + min(memo[j-1][0], memo[j-1][2])
            memo[j][2] = home[j][2] + min(memo[j-1][0], memo[j-1][1])
    print(min(memo[N-1]))
    
if __name__ == '__main__':
    solve()