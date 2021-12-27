#https://www.acmicpc.net/problem/1003
import sys

def Fibonacci(N):
    global cnt, Fibonacci_memo
    if N == 0:
        return [1, 0]
    if N == 1:
        return [0, 1]
    if N not in Fibonacci_memo: # 동적 계획법 중 메모이제이션 활용
        Fibonacci_memo[N] = [sum(x) for x in zip(Fibonacci(N-1),Fibonacci(N-2))]
        # 0과 1 사용에 대한 횟수를 출력
    return Fibonacci_memo[N]

def solve():
    global Fibonacci_memo
    input = sys.stdin.readline
    TC = int(input())
    Fibonacci_memo = {}
    cnt_list = []
    for _ in range(TC):
        cnt = Fibonacci(int(input()))
        cnt_list.append(cnt)
    for x in cnt_list:
        print("%s %s"%(x[0],x[1]))

if __name__=="__main__":
    solve()