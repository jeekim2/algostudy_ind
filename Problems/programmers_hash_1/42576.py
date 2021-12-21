#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(participant, completion):
    answer = 0 
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
            
        if i == len(completion)-1:
            return participant[-1]
            

