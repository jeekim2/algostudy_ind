# https://www.acmicpc.net/problem/10816
# 문제 : 숫자카드 N개와 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램
# 입력 : 첫째줄 = 숫자카드 개수 N, 둘째줄 = 숫자 카드에 적힌 정수
#       셋째줄 = M개의 정수, 넷째줄 = 상근이가 몇개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수
# 출력 : 첫째 줄에 입력으로 주어진 M개의 수에 대해 각 수가 적힌 숫자 카드 출력

''' 실패한 경우 : 시간초과 '''
''' 원인 : 이진탐색에서 원하는 숫자를 못 찾았을 때 시간초과 발생
해당 문제를 해결하기 위해 Lower/Upper Bound 알고리즘 사용 필요
- Lower Bound(원하는 값이 처음 나오는 위치)
- Upper Bound(원하는 값이 나오는 마지막 위치)
참조 - https://blog.naver.com/PostView.naver?blogId=jsm6616&logNo=222582280368&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView&userTopListOpen=true&userTopListCount=5&userTopListManageOpen=false&userTopListCurrentPage=1
'''
''' 실패 코드
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
    return None
'''
import sys

def upper_binary_search(card_list,target, start, end):
    while start < end:
        mid = (start + end)//2

        if card_list[mid] > target:
            end = mid
        elif card_list[mid] <= target:
            start = mid + 1
    return end

def lower_binary_search(card_list,target, start, end):
    while start < end:
        mid = (start + end)//2

        if card_list[mid] >= target:
            end = mid
        elif card_list[mid] < target :
            start = mid + 1
    return end

def solve():
    input = sys.stdin.readline
    N = int(input())
    card_n = list(map(int,input().split()))
    M = int(input())
    num_m = list(map(int,input().split()))
    
    card_n.sort() # 이진탐색 목적
    
    for val in num_m:
        upper = upper_binary_search(card_n, val, 0, len(card_n))
        lower = lower_binary_search(card_n, val, 0, len(card_n))
        ans = upper - lower
        print(ans, end = ' ')

''' Dic 사용한 풀이 방식 
def solve():
    input = sys.stdin.readline
    N = int(input())
    card_n = list(map(int,input().split()))
    M = int(input())
    num_m = list(map(int,input().split()))
    result_dic = {}
    
    for i in card_n:
        if i in result_dic:
            result_dic[i] += 1
        else:
            result_dic[i] = 1

    for j in num_m:
        if j in result_dic:
            print(result_dic[j], end= ' ')
        else:
            print(0, end = ' ')
'''

if __name__ == '__main__':
    solve()