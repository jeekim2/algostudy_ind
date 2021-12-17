# https://programmers.co.kr/learn/courses/30/lessons/42577

# Hash 문제임.
def solution(phone_book):
    dic = {}
    for phoneNum in phone_book:
        dic[phoneNum] = 0
    for phoneNum in phone_book:
        checker = ""
        for c in phoneNum[:-1]:
            checker += c
            if dic.get(checker) != None:
                return False
    return True


if __name__ == "__main__":
    print(solution(list(input().split())))
