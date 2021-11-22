#https://www.acmicpc.net/problem/1929

#에라토스테네스의 체를 통해 소수 구하기

def prime_number(N):
    # prime_max=1
    prime_list = [False]*2+[True]*(N-1)
    # while prime_max**2<=N:
        # prime_max+=1  -> int(N**0.5)로 대체
    for i in range(2,int(N**0.5)+1):
        if prime_list[i]:
            # for j in range(2*i,N+1,i):
                # prime_list[j] = False -> slicing으로 대체
            prime_list[2*i::i] = [False]*(N//i-1)
    return prime_list

def Problem_1929(M,N):
    # M,N = map(int,input().split())
    is_prime = prime_number(N)
    for i in range(M,N+1):
        if is_prime[i]:print(i)
