#https://www.acmicpc.net/problem/11279
#나중에 heapq 말고 직접 heap구현해서 풀어보기
import sys
import heapq
input= sys.stdin.readline
N = int(input())
heap = []
for i in range(N):
    A = int(input())

    if A:
        heapq.heappush(heap,(-A,A)) #파이썬에서는 MIN HEAP만 지원하기에 최대 값으로 변경 Y=-X
        #print("heap1",heap)
    else:                           #input 값 0
        if heap:
            print(heapq.heappop(heap)[1])   #튜플 값에 [1]값이 -값이 아닌 원래 값이기 때문
            #print("heap2",heap)
        else:
            print(0)
