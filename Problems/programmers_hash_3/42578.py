#https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 0

    dic = {}
    total = 1
    for name, kind in clothes:
        if kind in dic:
            dic[kind]= dic[kind]+1
        else:
            dic[kind]= 1

    for i in dic.values():
        total = total*(i+1)

    answer = total-1
    return answer