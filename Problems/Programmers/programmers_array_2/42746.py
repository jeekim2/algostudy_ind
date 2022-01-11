#https://programmers.co.kr/learn/courses/30/lessons/42746


def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x:x*3,reverse = True)
    answer = str(int("".join(numbers)))
    return answer

#주어진 숫자의 제한 사항이 numbers의 원소가 0~1000이기 때문에
# 각 자리에 대해 일의 자리라고 가정하고 STR 으로 타입 바꾼 뒤
# *3을 하면 각 자리수에 대한 최대값을 알 수 있게 됨
