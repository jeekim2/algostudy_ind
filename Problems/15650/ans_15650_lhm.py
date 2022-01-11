#https://www.acmicpc.net/problem/15650

from itertools import combinations

n,m = map(int,(input().split()))

temp = [i+1 for i in range(0,n)]
temp2 = list(combinations(temp,m))

for i in range(len(temp2)):
    for j in range(len(temp2[0])):
        print(temp2[i][j])#, end=" ")
    #print(" ")    

#주석을 빼야 출력 형식에 맞는거 같은데 오히려 주석처리를 해야 맞네요..