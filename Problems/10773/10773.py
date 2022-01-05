#https://www.acmicpc.net/problem/10773
import  sys
input = sys.stdin.readline
T = int(input())
temp =[]
for i in range(T):
    x = int(input())
    if x == 0:
        temp.pop()
    else:
        temp.append(x)

print(sum(temp))