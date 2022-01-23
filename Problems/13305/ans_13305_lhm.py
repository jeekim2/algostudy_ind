#https://www.acmicpc.net/problem/13305
import sys
input = sys.stdin.readline
T = int(input())

dist = list(map(int, input().split()))
reserve = list(map(int, input().split()))

ans = 0

for i in range(T-1):
    if reserve[i+1] >= reserve[i]:
        reserve[i+1] = reserve[i]
    ans = ans + reserve[i]*dist[i]

print(ans)