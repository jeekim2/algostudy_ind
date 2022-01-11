#https://www.acmicpc.net/problem/15649
from itertools import permutations
x,y = map(int,input().split())

a = [i+1 for i in range(0,x)]
    
b = list(permutations(a,y))


for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=" ")
        #print(" ")