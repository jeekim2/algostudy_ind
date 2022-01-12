#https://www.acmicpc.net/problem/1037
import sys
input = sys.stdin.readline

T = int(input())
temp = list(map(int, input().split()))
#temp.sort()
#ans = temp[0]*temp[-1]
ans= min(temp)*max(temp)
print(ans)