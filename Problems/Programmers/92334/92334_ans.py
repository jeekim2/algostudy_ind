#https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3

def solution(id_list, report, k):
    report = set(report)
    answer = {x:0  for x in id_list}
    reported = {x:0  for x in id_list}
    
    for x in report:
        reported[x.split()[1]]+=1
    for x in report:
        if reported[x.split()[1]]>=k:
            answer[x.split()[0]] +=1
            
    
    
    answer = list(answer.values())
    return answer