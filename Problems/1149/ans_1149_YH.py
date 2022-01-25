#https://www.acmicpc.net/problem/1149

def solve():
    N = int(input())
    RGB = []
    for _ in range(N):
        RGB.append(list(map(int, input().split())))
    # cost = [[1,1,1]]*N - 초기화 
    # 주의 필요 : 얉은 복사돼서 의도치 않게 i-1번째가 i번째로 복사되기 때문에 결과가 이상해짐
    cost = [[1,1,1] for i in range(N)] # cost에 대한 array 설정
    cost[0] = RGB[0] #[RGB[0][0], RGB[0][1], RGB[0][2]] - cost에 대한 초기화
    for i in range(1, N):
        cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + RGB[i][0] # 마지막에 Red를 칠하는 경우
        cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + RGB[i][1] # 마지막에 Green을 칠하는 경우
        cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + RGB[i][2] # 마지막에 Blue를 칠하는 경우
    print(min(cost[N-1][0],cost[N-1][1],cost[N-1][2]))

if __name__ == "__main__":
    solve()