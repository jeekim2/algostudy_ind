# https://www.acmicpc.net/problem/2775

# 문제 : a층의 b호에 살려면 a-1층의 1호부터 b호까지 사람 수의 합만큼 데려와야함.
# 아파트에 비어있는 집은 없음. 주어진 k와 n에 대해 k층 n호에 몇 명이 사는지 출력
# 입력 : Test case(T), k층, n호

def solve():
    test_n = int(input())
    
    for _ in range(test_n):
        floor_n = int(input())
        unit_n = int(input())
        sum_i = 0
        person_n =[]
        
        for i in range(1,unit_n+1):
            person_n.append(i) # 1층 거주 전체 인원
        for j in range(floor_n): # floor_n -> 실제 floor - 1 만큼 동작
            for k in range(1,unit_n):
                person_n[k] = person_n[k] + person_n[k-1]
        print(person_n[-1])
        
if __name__ == "__main__":
    solve()