#https://www.acmicpc.net/problem/2839
import sys
input = sys.stdin.readline
N = int(input())

fivekg = N//5
threekg = N//3

target_five = 0
target_three = 0
anschk = 0
ans = []
for i in range(fivekg+1):
    for j in range(threekg+1):
        if 5*i+3*j == N:
            target_five = i
            target_three = j
            ans +=[target_five+target_three]
            anschk = 1
if anschk == 0:
    print(-1)
else:
    print(min(ans))


