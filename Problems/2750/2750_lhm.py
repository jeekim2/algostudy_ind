#https://www.acmicpc.net/problem/2750
import sys
input = sys.stdin.readline
T = int(input())
array  =[]
for i in range(T):
    array.append(int(input()))

#array.sort()
for i in range(len(array)-1):
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]#i/j 동시변경
for i in range(len(array)):
    print(array[i])