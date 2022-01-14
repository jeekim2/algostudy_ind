# https://www.acmicpc.net/problem/1003

# ---------------------------------------------
# (1) 동적 계획법? 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법(분할)

# (2) 동적 계획법의 조건
# : 부분 반복 문제 (Overlapping Subproblem)
# - 계속해서 같은 부분문제(subproblem)가 여러번 재사용되거나 재귀 알고리즘을 통해 해결되는 문제
# : 최적 부분 구조 (optimal Substructure)
# - 작은 부분 문제에서 구한 최적의 답으로 합쳐진 큰 문제의 최적의 답을 구할 수 있어야 함.
# (예시) 피보나치 숫자

# (3) 메모이제이션(memoization)
# : 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거
# : 실행 속도를 빠르게 하는 기술로, 동적 계획법의 핵심이 되는 기술
# : 배열을 생성하고 계산한 값을 저장하여, 저장된 값일 경우 배열의 값을 리턴하는 방식으로 구현
# - 저장해 두는 메모리(배열) = 캐시 (Cache)라고 부름.

# (4) 접근 방법
# : Top-Down 방식
# - 재귀 호출을 이용하여 위에서 아래로 접근하는 방법 (큰 문제 -> 부분 문제)
# : Bottom-Up 방식
# - for를 이용하여 아래에서 위로 전급하는 방법 (부분 문제 -> 큰 문제)
# ---------------------------------------------

# method(1) - Bottom Up 방식
def fibo(x):
    if x == 0:
        return dp_num[0]
    elif x == 1:
        return dp_num[1]
    else:
        for i in range(2, x+1):
            dp_num[i] = [dp_num[i-1][0]+dp_num[i-2][0], dp_num[i-1][1]+dp_num[i-2][1]]
        return dp_num[i]

# method(2) - Top down 방식
def fibo2(x):
    global dp_num
    global fibo_memo
    
    if x == 0:
        return dp_num[0]
    if x == 1:
        return dp_num[1]
    if x not in fibo_memo: # 연산 값에 대해 memoization 수행
        fibo_memo[x] = [sum(x) for x in zip(fibo(x-1),fibo(x-2))]
    return fibo_memo[x]

def solve():
    global dp_num
    global fibo_memo

    result = dict()
    result2 = dict()
    fibo_memo = dict()
    
    dp_num = dict()    
    dp_num[0] = [1,0] # zero가 나오는 table 값
    dp_num[1] = [0,1] # one이 나오는 table 값
    
    test_n = int(input())
    
    for i in range(test_n):
        N = int(input())
        result[i]=fibo(N) # Bottom-up 방식 (For루프)
        result2[i]=fibo2(N) # Top-down 방식 (재귀함수)
    
    for j in range(test_n):
        print(*result[j])

    for k in range(test_n):
        print(*result2[k])

if __name__ == "__main__":
    solve()  # Dynamic Programming 해결 