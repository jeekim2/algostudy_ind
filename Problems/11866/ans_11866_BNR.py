'''
https://www.acmicpc.net/problem/11866
'''
import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    N_list = [i for i in range(1, N+1)]
    Result = []

    while N_list:
        for i in range(K-1):
            N_list.append(N_list.pop(0))    #3번째 수 전까지 pop으로 뒤에 붙이기
        Result.append(N_list.pop(0))  #3번째 수 다른 배열에 저장

    print("<", end="")
    for i in range(N-1):
        print(Result[i], end=", ")
    print(Result[N-1],end="")
    print(">")

if __name__ == "__main__":
    solve()