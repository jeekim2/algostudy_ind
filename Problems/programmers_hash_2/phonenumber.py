#https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):

    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]) == True:
            answer = False
    return answer

#startswith 모르면 풀기 어렵다