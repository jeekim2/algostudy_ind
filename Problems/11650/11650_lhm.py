#https://www.acmicpc.net/problem/11650
import sys
input = sys.stdin.readline
T = int(input())
temp = []
ans = []


for i in range(T):
    [x,y] = map(int,input().split())
    temp.append([x,y])

#temp.sort()

def quick_sort(list):
    if len(list) <=1 : return list
    pivot = list[len(list)//2]
    less_arr, equal_arr, big_arr = [],[],[]
    for i in list:
        if i < pivot : less_arr.append(i)
        elif i > pivot : big_arr.append(i)
        else: equal_arr.append(i)
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)


ans = quick_sort(temp)



for i in range(len(ans)):
    print(ans[i][0], ans[i][1])