# https://www.acmicpc.net/problem/10816
# 문제 : 숫자카드 N개와 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램
# 입력 : 첫째줄 = 숫자카드 개수 N, 둘째줄 = 숫자 카드에 적힌 정수
#       셋째줄 = M개의 정수, 넷째줄 = 상근이가 몇개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수
# 출력 : 첫째 줄에 입력으로 주어진 M개의 수에 대해 각 수가 적힌 숫자 카드 출력

import sys

def binary_search(card_list,target, start, end):
    while start <= end:
        mid = (start + end)//2

        if card_list[mid] == target:
            return card_list[start:end+1].count(target)
        elif card_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

def solve():
    input = sys.stdin.readline
    N = int(input())
    card_n = list(map(int,input().split()))
    M = int(input())
    num_m = list(map(int,input().split()))
    
    card_n.sort() # 이진탐색 목적
    
    for val in num_m:
        start = 0
        end = len(card_n) - 1
        ans = binary_search(card_n, val, start, end)
        if ans != None:
            print(ans, end = ' ')
        else:
            print(0, end = ' ')

if __name__ == '__main__':
    solve()