#https://www.acmicpc.net/problem/10610
import sys
input = sys.stdin.readline
N = input()
N = list(N)
chk = 0
sum_N = 0
ans = ""
for i in range(len(N)-1):
    if N[i] == "0": 
        chk =1
    sum_N+=int(N[i])

if sum_N%3 ==0 and chk ==1:
    N.sort(reverse=True)
    for i in range(len(N)-1):
        ans+=N[i]
    print(int(ans))
else:
    print(-1)
