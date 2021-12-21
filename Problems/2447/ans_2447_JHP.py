# https://www.acmicpc.net/problem/2447
# 문제 : pattern : ["***","* *","***"]으로 둘러싸인 N//3 정사각형 만들기
# 분할 정복 알고리즘 = 분할, 정복, 합치기
# 분할 정복 알고리즘: 문제를 나눌 수 없을 때까지 나누어서 각각 풀면서 다시 합병하여 문제의 답을 얻는 알고리즘

import sys

def star(N):
    pat_arr=[]
    # print(len(N))
    for i in range(3*len(N)):
        if i // len(N) == 1: # 정사각형으로 둘러쌓이는 구간 처리
            pat_arr.append(N[i%len(N)] + " "*len(N) + N[i%len(N)])
        else:
            pat_arr.append(N[i%len(N)]*3)
    return list(pat_arr)

def solve():
    input = sys.stdin.readline
    N = int(input())
    k = 0
    pat = ["***","* *","***"]  # n=3 일때, 최소 분할 단위

    while N!=3:
        N = int(N//3)
        k += 1
    
    for i in range(k):
        pat = star(pat)
    for val in pat:
        print(val)
    
if __name__ == "__main__":
    solve()
