#https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == True:
            answer+=absolutes[i]
        else:
            answer+=-1*absolutes[i]

    return answer