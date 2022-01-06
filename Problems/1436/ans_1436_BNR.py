# https://www.acmicpc.net/problem/1436

# import sys  #재귀로 풀려 했더니 런타임에러남. 파이썬에서 재귀 depth는 1000임. 변경할 수 있지만 메모리초과 발생
# sys.setrecursionlimit(10**6) 

# N = int(input())
# global t
# t =0

# def final(idx,N_movie):
#     global t
#     if '666' in str(idx):
#         t += 1
#         if t == N_movie:
#             print('number',idx)
#             return idx
#     final(idx+1,N_movie)

# final(1,N)


N = int(input())
t =0
idx = 0
while t != N:
    if '666' in str(idx):
        t += 1
        if t == N:
            print(idx)
    idx += 1