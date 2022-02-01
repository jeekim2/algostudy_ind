# https://www.acmicpc.net/problem/11054
# 문제 : 가장 긴 바이토닉 부분 수열
# 입력 : 첫째 줄 = 수열 크기 N, 둘째 줄 = 수열 A
# 출력 : 첫째 줄에 수열 A의 가장 긴 바이토닉 부분 수열의 길이
# 접근 : A[j] < A[i]일 경우 -> 올림 수열
# 접근 : max

import sys
from unittest import result

def seq_cnt(N):
    global A
    memo_a = [1]*N
    memo_d = [1]*N
    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                memo_a[i] = max(memo_a[i], memo_a[j]+1)
    
    for idx, cnt in enumerate(memo_a):
        if cnt == max(memo_a):
            temp_idx = idx

    for i in range(N-1,temp_idx-1,-1):
        for k in range(N-1,i,-1):
            if A[k] < A[i]:
                memo_d[i] = max(memo_d[i], memo_d[k]+1)
    ans = max(memo_a)+max(memo_d)-1
    return ans

def solve():
    global A
    
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int,input().split()))
    
    print(seq_cnt(N))

if __name__ == "__main__":
    solve()