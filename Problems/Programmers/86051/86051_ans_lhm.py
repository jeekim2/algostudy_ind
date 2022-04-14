#https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    temp = [0,1,2,3,4,5,6,7,8,9]
    answer = sum(set(temp) -set(numbers))
    return answer