'''
https://www.acmicpc.net/problem/12015

가장 긴 증가하는 부분 수열
'''
import sys

def bs(A_num, LIS):
    if LIS[-1]<A_num:
        LIS.append(A_num)
        return LIS
    else:
        left = 0
        right = len(LIS)
        while left<right:
            mid = (left+right)//2
            if LIS[mid] < A_num:
                left = mid+1
            else:
                right = mid
                idx = right
        LIS[idx] = A_num
    return LIS

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int,input().split()))
    LIS = [A[0]]
    for i in range(1,N):
        bs(A[i], LIS)
    print(len(LIS))

if __name__ == "__main__":
    solve()