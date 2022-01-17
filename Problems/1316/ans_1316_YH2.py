#https://www.acmicpc.net/problem/1316
#Dictionary 이용한 2번째 풀이 
import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    cnt = 0
    for _ in range(N):
        char_var = input()
        check = {char_var[0]:True} #check : 입력 문자에 대한 사용 여부 확인 
        cnt+=char_chk(char_var,check)
    print(cnt)

def char_chk(char, check):
    for i in range(1,len(char)):
        if char[i-1] == char[i] : continue #연속된 문자열 case
        if char[i] in check : return 0 #연속되지 않은 문자열+이미 사용된 문자 case
        check[char[i]] = True #문자 사용 입력
    return 1

if __name__ == "__main__":
    solve()