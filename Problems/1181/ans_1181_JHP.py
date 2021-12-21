# https://www.acmicpc.net/problem/1181
# 문제 : 알파벳 소문자로 이루어진 N개의 단어가 들어올 경우, 아래 조건에 따라 정렬
# (1) 길이가 짧은 것부터, (2) 길이가 같으면 사전 순으로
# 입력 : 첫줄 = 단어 개수 N, 둘째 줄= N개의 소문자 단어
# 추력 : 초전에 따라 정렬하는 단어 출력

import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    word = []
    
    for i in range(N):
        word.append(input())
        # print(word)
    
    temp = set(word) # 중복 문자 제거 방법
    # print(temp)
    word = list(temp) # sort를 위해 list로 변경
    
    word.sort()
    word.sort(key=len)
    # print(word)
    
    for i in word:
        print(i,end= "")

if __name__ == '__main__':
    solve()