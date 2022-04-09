# https://www.acmicpc.net/problem/1920
# 문제 : N개의 숫자 Array (A)가 주어지고, M개의 숫자가 주어졌을 떄 해당 숫자가 A에 있는지 확인하는 문제
# 입력 : 첫째줄 = N, 둘쨰줄 = N개의 숫자 Array, 셋째줄 = M, 넷째줄 = M개의 숫자
# 출력 : M개의 숫자가 Array A에 있는지 여부 판단 (True = 1, False = 0)

import sys

def binary_search(reference,target, left, right):
    if left > right:
        return 0

    mid = (left + right)//2

    if target < reference[mid]:
        return binary_search(reference,target,left,mid-1)
    elif target > reference[mid]:
        return binary_search(reference,target,mid+1,right)
    else: 
        return 1

def solve():
    input = sys.stdin.readline
    N = int(input())
    array_n = list(map(int,input().split()))
    M = int(input())
    array_m = list(map(int,input().split()))
    
    array_n.sort()

    for val_m in array_m:
        print(binary_search(array_n,val_m, 0, N - 1))
        
if __name__ == "__main__":
    solve()
