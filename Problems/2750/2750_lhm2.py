#https://www.acmicpc.net/problem/2750
T = int(input())
array  =[]
for i in range(T):
    array.append(int(input()))

array.sort()


for i in range(len(array)):
    print(array[i])