#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        if i == len(completion) - 1:
            return participant[-1]

#문제를 잘못 이해함, 1명만 차이나는 것을 못봄 
#좋은 답변
'''
import collections

def solution(participant, completion):
    participant.sort()
    completion.sort()
    ans = collections.counter(participant)-collections.counter(completion)
    result list(result)[0]
'''