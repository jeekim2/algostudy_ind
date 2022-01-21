'''
https://www.acmicpc.net/problem/9461
'''
N = int(input())
TC = []

for i in range(N):
    TC.append(int(input()))

global p
p =[0]*(101)    #입력 범위 100까지

p[1] = 1
p[2] = 1
p[3] = 1

def padovan(num):
    for num in range(4, num+1):
        p[num] = p[num-2]+p[num-3]
    return print(p[num])

for i in TC:
    padovan(i)
