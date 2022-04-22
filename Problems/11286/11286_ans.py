#https://www.acmicpc.net/problem/11286
#heapq 활용, 파이썬 지원 heapq는 최소힙
#다음에는 heapq 활용하지 않고 풀어보기
import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    a = int(input())

    if a != 0:
        heapq.heappush(heap, (abs(a), a))   #절대값 작은수 때문에 tuple 넣음
    
    else:
        if len(heap) == 0:
            print(0)
        else:
            #print("ans:")
            print(heapq.heappop(heap)[1])
    #print(i,"번째",heap)