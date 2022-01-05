#https://www.acmicpc.net/problem/15650
'''
from itertools import combinations

n,m = map(int,(input().split()))

temp = [i+1 for i in range(0,n)]
temp2 = list(combinations(temp,m))

for i in range(len(temp2)):
    for j in range(len(temp2[0])):
        print(temp2[i][j])#, end=" ")
    #print(" ")    
'''
#주석을 빼야 출력 형식에 맞는거 같은데 오히려 주석처리를 해야 맞네요..
#15649와 상당히 유사한 문제인데, dfs 함수 안에 인덱스를 넣어서 겹치지 않게 해주면 될 듯 합니다
import sys
input= sys.stdin.readline
n, m = map(int, input().split())    #ex)n=3, m=1

arr = [] #stack 개념, 길이 맞으면 출력

def dfs(x):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(x, n+1):
        if i in arr:
            continue
        if (len(arr)>=1 and i<arr[-1]):
            continue
        arr.append(i)
        dfs(x+1)#재귀
        arr.pop()

dfs(1) 