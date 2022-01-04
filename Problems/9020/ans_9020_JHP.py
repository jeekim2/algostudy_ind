# https://www.acmicpc.net/problem/9020
# 문제 : (골드바흐의 추측) 2보다 큰 모든 짝수는 두 소수의 합으로 표현 가능 = 골드바흐 수. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션 존재
# 2~n이 주어졌을때, 두 소수의 차이가 가장 작은 n의 골드바흐 파티션을 출력하는 프로그램 작성

def primeNum(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solve():
    test_n = int(input())
    num = []
    
    for i in range(test_n):
        n = int(input())
        num.append(n)
    
    for val in num:
        for i in range(val//2, 1, -1): # 소수의 차이가 작은거부터 출력하기 위해 역순으로 확인
            if primeNum(i) and primeNum(val-i):
                print(i,val-i)
                break

if __name__ == "__main__":
    solve()