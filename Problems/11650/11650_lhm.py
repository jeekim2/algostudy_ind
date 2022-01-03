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

while temp:
    ans.append(min(temp))
    temp.pop(temp.index(min(temp)))
##위에 whlie temp 부분이 sort 대신쓰려고 넣은건데 계속 시간 초과 가 뜨네.... 왜그런지 아시는분



for i in range(len(ans)):
    print(ans[i][0], ans[i][1])
