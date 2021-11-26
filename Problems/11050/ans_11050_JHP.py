# https://www.acmicpc.net/problem/11050

# 문제 : 이항계수 N/K를 구하는 프로그램 작성
# 이항 계수란? N! / (N-K)! K!

# 아래 For를 이용하면 Run time Error 발생
# 따라서, 재귀함수의 활용하는 것으로 Runtime Error를 방지할 필요가 있음. (재귀로 다시 풀어보자)

def solve():
    N, K = list(map(int,input().split()))
    temp_N = []
    temp_K = []
    temp_S = []
    
    for i in range(1,N+1):
        temp_N.append(i)
        
    for j in range(1,K+1)
        temp_K.append(j)
        
    for k in range(1,(N-K)+1):
        temp_S.append(k)
        
    print(temp_N)
    print(temp_K)
    print(temp_S)    
    
    for i in range(0,len(temp_N)):
        if i == 0:
            fact_N = temp_N[0]
        else :
            fact_N = fact_N*temp_N[i]

    for j in range(0,len(temp_K)):
        if j == 0:
            fact_K = temp_K[0]
        else:
            fact_K = fact_K*temp_K[j]
            
    for k in range(0,len(temp_S)):
        if k == 0:
            fact_S = temp_S[0]
        else:
            fact_S = fact_S*temp_S[k]
    
    print(fact_N)
    print(fact_K)
    print(fact_S)
    
    result = fact_N / (fact_S * fact_K)
    print(result)

if __name__ == "__main__":
    solve()