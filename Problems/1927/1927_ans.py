#https://www.acmicpc.net/problem/1927

import sys
import heapq

input = sys.stdin.readline

N = int(input())
min_heap = []

for i in range(N):
    n = int(input())

    if n == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap))
        else:
            print(0)

    else:
        heapq.heappush(min_heap,n)