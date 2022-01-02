#https://www.acmicpc.net/problem/15649
'''
from itertools import permutations
x,y = map(int,input().split())

a = [i+1 for i in range(0,x)]
    
b = list(permutations(a,y))


for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=" ")
        #print(" ")
'''
n, m = map(int, input().split())    #ex)n=3, m=1

arr = [] #stack 개념, 길이 맞으면 출력

def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        if i in arr:
            continue
        arr.append(i)
        dfs()#재귀
        arr.pop()

dfs()