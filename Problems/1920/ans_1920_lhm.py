#https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline
N = int(input())
Array_N = sorted(list( map(int,input().split())))
#sorted 말고 다른 정렬 방법으로 푸는 것도 고려 필요
#이진 탐색은 찾고자 하는 대상이 순차 정렬이 되어 있어야 함
M = int(input())
Array_M = list( map(int, input().split()))


for i in range(M):

    start = 0
    end = N -1
    mid = (start+end)//2
    result = 0

    while end - start >=0:
        if Array_N[mid] == Array_M[i]:
            result =1
            break
        elif Array_N[mid] < Array_M[i]:
            start = mid + 1
        elif Array_N[mid] > Array_M[i]:
            end = mid -1
        mid = (start + end )//2
    print(result) 
