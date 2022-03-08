# https://www.acmicpc.net/problem/1300

# K번째 수

# N*N의 배열을 만들면 메모리 초과
# 접근 1: A를 구하고 B배열에 이분탐색으로 정렬 -> 시간 초과
# 접근 2: K 이하의 수의 갯수로 접근해야함... 

import sys

def bs1(num, B):        #시간 초과
    left = 0
    right = len(B)

    while left<=right:
        mid = (left+right)//2
        if num>=mid:    #수가 mid보다 크면 left크게
            left = mid+1
        else:
            right = mid-1
    
    B.insert(right,num)
    return B

def bs2(N,K):
    left = 0
    right = K
    result = 0
    while left<=right:
        mid = (left+right)//2
        count = 0
        for i in range(1, N+1):
            count += min(mid//i, N)
        if count <K:
            left = mid+1
        else:
            result = mid
            right = mid-1
    return result

def solve():
    input = sys.stdin.readline
    N = int(input())
    K = int(input())
    
    print(bs2(N,K))

    # B = []    #시간초과(for문 1개로 줄여도 시간초과)  
    # for i in range(N):  # A배열 값
    #     for j in range(N):
    #         A = (i+1)*(j+1) 
    #         bs1(A, B)
    #print(B[K-1]) # 1부터 인덱스 시작

if __name__ == "__main__":
    solve()