#https://www.acmicpc.net/problem/1003
import sys
# 시간초과
# 최적화 필요

def Fibonacci(N):
    global cnt0, cnt1
    if N == 0:
        cnt0+=1
        return 0
    if N == 1:
        cnt1+=1
        return 1
    return Fibonacci(N-1)+Fibonacci(N-2)

def solve():
    input = sys.stdin.readline
    global cnt0, cnt1
    TC = int(input())
    cnt_list = []
    for _ in range(TC):
        cnt0=cnt1=0
        N = int(input().rstrip())
        Fibonacci(N)
        cnt_list.append((cnt0,cnt1))
    print("\n".join(map(str, cnt_list)))

if __name__=="__main__":
    solve()