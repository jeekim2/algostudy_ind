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

for i in range(len(temp)-1):
    for j in range(i+1,len(temp)):
        if temp[i][0] > temp[j][0]:
            temp[i][0], temp[j][0] = temp[j][0], temp[i][0]
            temp[i][1], temp[j][1] = temp[j][1], temp[i][1]

for i in range(len(temp)-1):
    for j in range(i+1,len(temp)):
        if temp[i][1] > temp[j][1]:
            temp[i][0], temp[j][0] = temp[j][0], temp[i][0]
            temp[i][1], temp[j][1] = temp[j][1], temp[i][1]


for i in range(len(temp)):
    print(temp[i][0], temp[i][1])
