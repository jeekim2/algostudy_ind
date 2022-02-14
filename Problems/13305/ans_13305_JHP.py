# https://www.acmicpc.net/problem/13305
# 문제 : 최소 주유 비용을 계산하는 프로그램 작성
# 입력 : 첫째줄 - 도시 개수, 둘째줄 - 각 도시별 거리, 셋째줄 - 주유소의 리터당 가격
# 출력 : 제일 왼쪽 도시에서 제일 오른쪽 도시까지 가는 최소 비용

def solve():
    N = int(input())
    dist = list(map(int,input().split()))
    price = list(map(int,input().split()))
    
    cost = 0
    temp_cost = 1000000001
    
    for i in range(len(price)-1):
        temp_cost = min(temp_cost, price[i])
        cost += temp_cost*dist[i]
    
    print(cost)
    
if __name__ == "__main__":
    solve()