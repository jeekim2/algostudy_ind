# https://www.acmicpc.net/problem/14888
# 백트래킹 알고리즘
# 문제 : N개의 수로 이루어진 수열 A1,A2,...An이 있고, 그 사이에 N-1개의 연산자가 있음.
# 주어진 수의 순서를 바꾸지 않고 수식을 만들어서 최대/최소 값을 구하는 문제

# 입력 : 첫째 줄 = N(숫자 개수), 둘째 줄 = A1,A2,...,An, 셋째 줄 = 합이 N-1인 4개의 정수(+,-,x,%)
# 출력 : 첫째 줄 = 최댓값, 둘째 줄 = 최솟값 출력

import sys

def calculation(index,cal,plus,minus,multiple,divide):
    global n, num, operator,result
            
    if index == n:
        result.append(cal)
        return result
    else:
        if plus:
            calculation(index+1, cal + num[index], plus-1,minus,multiple,divide)
        if minus:
            calculation(index+1, cal - num[index], plus,minus-1,multiple,divide)
        if multiple:
            calculation(index+1, cal * num[index], plus,minus,multiple-1,divide)
        if divide:
            calculation(index+1, int(cal / num[index]), plus,minus,multiple,divide-1)

def solve():
    global n, num, operator,result
    
    input = sys.stdin.readline
    num = []
    operator = []
    result = []
    
    n = int(input())
    num = list(map(int,input().split()))
    operator = list(map(int,input().split()))
    
    calculation(1,num[0],operator[0],operator[1],operator[2],operator[3])
    
    print(max(result))
    print(min(result))

if __name__ == "__main__":
    solve()