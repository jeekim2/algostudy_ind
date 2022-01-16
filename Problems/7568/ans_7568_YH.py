#https://www.acmicpc.net/problem/7568


import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    person = []
    for _ in range(N):
        # person.append(list(input().split())) 
        # - input()은 엄연히 문자열이며, person은 문자열의 리스트들을 요소로 가져감
        # - 입력에 따른 출력은 T/C에 맞게 표출되지만, 결론적으로 백준에서는 "틀렸습니다."로 판정
        # - 문자열에서 정수로 변경하는 단계 누락없도록 신경써야 함. 반례 찾는다고 개고생....
        person.append(list(map(int, input().split())))

    for p1 in person:
        rating = 1
        for p2 in person:
            if p1 == p2 : continue
            if (p1[0] < p2[0]) and (p1[1] < p2[1]):
                rating+=1
        print(rating, end = " ") 

if __name__=="__main__":
    solve()
