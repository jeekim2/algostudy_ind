#https://www.acmicpc.net/problem/11650
import sys
input = sys.stdin.readline
T = int(input())
temp = []


for i in range(T):
    [x,y] = map(int,input().split())
    temp.append([x,y])

temp.sort()


for i in range(len(temp)):
    print(temp[i][0], temp[i][1])
   