#https://programmers.co.kr/learn/courses/30/lessons/42842
#내가 푼거, Test case 77점
def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    temp = []
    temp_index =[]

    for i in range(2,sum):
        if sum%i == 0:
            temp.append(i)

    while len(temp)>2:
        temp.remove(min(temp))
        temp.remove(max(temp))

    answer.append(max(temp))
    answer.append(min(temp))

    return answer

#남이 푼거
def solution(brown,yellow):
    s= brown+yellow
    for i in range(s,2,-1):
        if s%i == 0:
            a=s//i
            if yellow ==(i-2)*(a-2):
                return[i,a]
#가로,세로 더한뒤에 만들수 있는 약수 중 비슷한 2수 ( 중간값 2개) 고르면 될줄 알았지만
#실제문제는 yellow 값이 가로 세로 각각 2개를 뺀 것과 같게 해야됨