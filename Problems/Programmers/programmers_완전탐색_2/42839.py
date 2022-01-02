#https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations
def solution(numbers):
    answer = 0
    #에라토스테네스의 체 ( 소수 구하는 방법)
    Max = 10000000 # 최대 7자리수
    check = [True]*(Max)  #구하려는 모든 수에 대해서 True로 채워넣기
    check[0] = check[1] = False # 0,1은 소수가 아님

    for i in range(2,Max):
        if check[i] == True:
            for j in range(i*2,Max,i): #2~최대값 까지 각각 2,3,4의 배수를 다 False 처리
                check[j]=False  #True로 남아 있는 건 다 소수

    #문자열로 숫자 만들기 / 123이 있다고 하면 1,2,3으로 나눠서 조합
    number = list(numbers)
    num = []
    for i in range(len(number)):
        num.append(list(set(map(''.join, permutations(number,i+1)))))

    num_list = list(set(map(int, sum(num,[]))))

    #문자열과 소수 체크
    for i in num_list:
        if check[i] == True:
            answer = answer+1
    return answer


