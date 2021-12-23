#https://www.acmicpc.net/problem/2798
T, Target =map(int,input().split())

Num = list(map(int,input().split()))

#i, j, k 3개의 서로 다른 수를 뽑자
result = 0
for i in Num:
    for j in Num:
        if i == j:
            continue
        for k in Num:
            if k == i or k == j :
                continue
            sum = i + j + k
            if sum > Target:
                continue
            if sum > result:
                result = sum

print(result)