#https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0]<K:
        if len(scoville)>1:
            heapq.heappush(scoville,heapq.heappop(scoville)+2*heapq.heappop(scoville))
            answer+=1
        else:
            return-1
    
    return answer