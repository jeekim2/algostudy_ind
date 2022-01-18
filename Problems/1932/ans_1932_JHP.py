# https://www.acmicpc.net/problem/1932
# 문제 : 삼각 피라미드의 합이 최대가 되는 경로 찾기
# 입력 : 첫째 줄 = 삼각형의 크기, 둘째 줄 = n+1번째 줄까지 정수 삼각형
# 출력 : 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합

def solve():
    n = int(input())
    floor_num = []

    
    for _ in range(n):
        floor_num.append(list(map(int,input().split())))
    level = 2
    
    for i in range(1,n):
        for j in range(level): # n+1번째 줄까지
            if j == 0: # 맨 첫번째 숫자
                floor_num[i][j] += floor_num[i-1][j]
            elif j == i: # 맨 마지막 숫자 (정삼각형이므로)
                floor_num[i][j] += floor_num[i-1][j-1]
            else: # 가운데 숫자
                floor_num[i][j] += max(floor_num[i-1][j-1],floor_num[i-1][j]) # 더 큰 숫자를 더하기 위함.
        level += 1
    print(max(floor_num[-1])) # 마지막 합의 최종 숫자 중 큰 수 출력

if __name__ == "__main__":
    solve()