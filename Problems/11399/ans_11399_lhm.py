#https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

def quick_sort(a):  #퀵소트
    n = len(a)
    if n <=1:
        return a
    
    pivot = a[-1] #pivot 값 임시 지정
    s1 = []
    s2 = []

    for i in range(0, n-1):
        if a[i]<pivot:
            s1.append(a[i])
        else:
            s2.append(a[i])

    return quick_sort(s1)+[pivot]+quick_sort(s2)

T = int(input())
b = list(map(int,input().split()))
b.sort()
#b = quick_sort(b) # 퀵소트 쓰면 런타임 에러 뜨네..

for i in range(1,len(b)):
    b[i] = b[i-1]+b[i]


print(sum(b))
