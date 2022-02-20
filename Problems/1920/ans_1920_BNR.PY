'''
https://www.acmicpc.net/problem/1920

바이너리 정렬(이진 삽입 정렬) 이용
'''

import sys

def merge(left, right):
    i = 0
    j = 0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
    
def merge_sort(list):   #sort
    if len(list)<=1:
        return list
    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left,right)

def binary_search(array,target,start,end):  #binary search, 정렬된 리스트만 사용가능
    while start<=end:
        mid = (start+end)//2 #중간 인덱스
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return 0

def solve():
    N = int(sys.stdin.readline())
    N_array =  list(map(int, sys.stdin.readline().split()))
    sorted_N_array = merge_sort(N_array)   #sort 오름차순 정렬
    # N_array.sort()
    M = int(sys.stdin.readline())
    M_array =  list(map(int, sys.stdin.readline().split()))

    for i in range(M):
        print(binary_search(sorted_N_array,M_array[i],0,N-1))


if __name__ == "__main__":
    solve()