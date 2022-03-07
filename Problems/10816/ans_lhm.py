#https://www.acmicpc.net/problem/10816

import sys

input = sys.stdin.readline

N = int(input())
N_array = list(map(int, input().split()))

M = int(input())
M_array = list(map(int, input().split()))

N_array.sort()
ans = {} #dic 사용
#N_array 를 dic 형태 ( ans )로 변환
for i in N_array:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] = ans[i]+1
#ans dic 처리 순서를 바꾸면 시간 초과되네요.. 연산하는게 생각보다 시간을 꽤먹나봅니다

for i in M_array:
    start = 0
    end = N-1

    while end-start>=0:
        mid = (start+end)//2
        if i == N_array[mid]:
            break
        elif i> N_array[mid]:
            start = mid+1
        else:
            end = mid -1
    if i== N_array[mid]:
        print(ans[i],end =" ")
    else:
        print(0,end = " ")
