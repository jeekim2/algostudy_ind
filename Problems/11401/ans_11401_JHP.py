# https://www.acmicpc.net/problem/11401
# 문제 : 자연수 N, 정수 K가 주어졌을 때, 이항계수를 1,000,000,007로 나눈 나머지 구하기
# 입력 : N과 K가 주어짐
# 출력 : 출력 N, K 이항계수를 1,000,000,007로 나눈 값
# 이항 계수란? N! / (N-K)! K!
# (Runtime error 해결 목적) 페르마 소정리 적용 필요 
'''페르마 소정리
p가 소수이고 a와 p가 서로소이면 a^(p-1) = 1(mod p)'''

import sys

def factorial(num, p): # runtime error 발생함
    if num <= 1:
        return 1
    else:
        temp = ((num*factorial(num-1,p))%p)
        return temp

def perma(num,s,p):
    if s == 1:
        return num % p
    if s%2 == 0:
        temp = perma(num,s//2,p)
        return (temp*temp)%p
    else:
        temp = perma(num,s//2,p)
        return (temp*temp*num)%p 

def solve():
    input = sys.stdin.readline
    N, K = map(int,input().split()) 
    p = 1000000007
    fact_N = 1
    fact_K = 1
    fact_NK = 1    
    for i in range(1,N+1):
        fact_N = (fact_N*i)%p
    for i in range(1,K+1):
        fact_K = (fact_K*i)%p
    for i in range(1,N-K+1):
        fact_NK = (fact_NK*i)%p
    # 아래 factorial 사용했을 때, 결과는 맞지만 runtime error 발생
    # fact_N = factorial(N,p)
    # fact_K = factorial(K,p)
    # fact_NK = factorial(N-K,p)
    fact_K = perma(fact_K, p-2, p)
    fact_NK = perma(fact_NK, p-2, p)
    result = (fact_N * fact_K * fact_NK)   
    print(result % p)

if __name__ == "__main__":
    solve()