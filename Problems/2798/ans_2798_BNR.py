#https://www.acmicpc.net/problem/2798

N,M = map(int, input().split()) #N개수, M을 넘지 않는
N_List = list(map(int, input().split()))
max = 0

for _ in range(N-2):
    i = N_List[_]
    for __ in range(_+1,N-1):
        j = N_List[__]
        for ___ in range(__+1,N):
            k = N_List[___]
            tmp = i+j+k
            if tmp>max and tmp<=M:
                max = tmp
print(max)