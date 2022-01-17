#https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

def quick_sort(a):  #퀵소트
    
    if len(a) <=1:
        return a

    pivot = a[len(a)//2] #pivot 값 임시 지정
    s1 = []
    s2 = []
    s =[]
    for i in a:
        if i<pivot:
            s1.append(i)
        elif i>pivot:
            s2.append(i)
        else:
            s.append(i)
    #print("a:",a)
    #print("pivot:",pivot)
    #print("s1:",s1)
    #print("s2:",s2)
    #print("s:",s)
    return quick_sort(s1)+s+quick_sort(s2)

T = int(input())
b = list(map(int,input().split()))
#b.sort()
b = quick_sort(b)


for i in range(1,len(b)):
    b[i] = b[i-1]+b[i]


print(sum(b))
