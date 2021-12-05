#https://www.acmicpc.net/problem/2751
""" input() vs sys.stdin.readline()
input() 내장 함수는 parameter로 prompt message를 받을 수 있다. 
따라서 입력받기 전 prompt message를 출력해야 한다. 
물론 prompt message가 없는 경우도 있지만, 이 경우도 약간의 부하로 작용할 수 있다. 
하지만, sys.stdin.readline()은 prompt message를 인수로 받지 않는다.
또한, input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴한다. 
즉 입력받은 문자열에 rstrip() 함수를 적용시켜서 리턴한다. 
반면에 sys.stdin.readline()은 개행 문자를 포함한 값을 리턴한다. 
결론적으로 input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고, 
개행 문자를 삭제한 값을 리턴하기 때문에 느리다.
"""
import sys

# (1) 순차 정렬(Sequential sort) - 시간 초과
# - 맨 앞에서부터 뒤의 요소들과 비교하여 작은 것을 발견하면 교환
# - 앞에서 가장 작은 값을 정렬해가는 방식
# - 시간복잡도 O(N^2)
# def solve():
#     N = int(sys.stdin.readline().strip())
#     num_list=[]
#     while len(num_list)< N:        
#         num_list.append(int(sys.stdin.readline().strip()))
    
#     for i in range(len(num_list)-1):
#         for j in range(i+1, len(num_list)):
#             if num_list[i] > num_list[j]:
#                 num_list[i], num_list[j] = num_list[j], num_list[i]
#     for x in num_list : 
#         print(x)

# (2) 선택 정렬(Selection sort)
#  - 첫번째부터 순차적으로 최소값 찾아 교환하기 = 순차 정렬과 같은 개념으로 보임.
#  - 첫번째에 가장 작은 수를 두고, 두번째에 두번째 작은 수를 둔다.
# - 시간복잡도 O(N^2) 
# def solve() :
#     Arry = [9, 8, 1, 3, 2]
    
#     for i in range(len(Arry)-1):
#         minIndex = i
#         for j in range(i+1, len(Arry)):
#             if Arry[j]<Arry[minIndex]:
#                 minIndex = j
#         Arry[i], Arry[minIndex] = Arry[minIndex], Arry[i]
#     print(Arry)

# (3) 버블 정렬(Bubble Sort)
# - 인접한 두 요소를 비교 및 교환해가면서 최대값 찾기
# - 가장 큰 수는 마지막에 두고, 두번째 큰 수는 마지막에서 두번째에 두기
# - 시간복잡도 O(N^2)
# def solve():
#     Arry = [9, 8, 1, 3, 2]
    
#     for i in range(1, len(Arry)):
#         for j in range(len(Arry)-i):
#             if Arry[j] > Arry[j+1]:
#                 Arry[j], Arry[j+1] = Arry[j+1], Arry[j]
#     print(Arry)
# (4) 삽입 정렬(Insertion Sort)
#  - 정렬된 구간과 정렬되지 않은 구간을 나눔 
#  - 정렬되지 않은 구간의 맨 앞 요소를 정렬된 구간에 삽입
#  - 시간복잡도 O(N^2) 
# 어렵다...ㅠ              
# def solve():
#     Arry = [9, 8, 1, 3, 2]
    
#     for i in range(1,len(Arry)):
#         key = Arry[i]
#         j=i-1 #key의 왼쪽 : i-1까지는 정렬되어 있는 상태
#         while j>=0 and Arry[j]>key:
#             Arry[j+1]=Arry[j]
#             j-=1
#         Arry[j+1] = key
#     print(Arry)
# (5) 병합 정렬(Merge Sort)
#  - 요소 1개까지 온전히 나누고, 다시 단계별로 couple로 묶으면서 정렬
# 점점 더 어려워지는구만....
# def merge(left, right):
#     result = []
#     while len(left)>0 or len(right)>0:
#         if len(left)>0 and len(right)>0:
#             if left[0]<=right[0]:
#                 result.append(left[0])
#                 left = left[1:]
#             else:
#                 result.append(right[0])
#                 right = right[1:]
#         elif len(left)>0:
#             result.append(left[0])
#             left = left[1:]
#         elif len(right)>0:
#             result.append(right[0])
#             right = right[1:]
#         else:
#             pass
#     return result

# def solve(Arry):
#     if len(Arry)<=1:
#         return Arry
#     mid = len(Arry)//2
#     leftArea = Arry[:mid]
#     rightArea = Arry[mid:] 
#     leftArea=solve(leftArea)
#     rightArea=solve(rightArea)
    
#     return merge(leftArea,rightArea)
# (6) 퀵 정렬(Quick Sort)
#  - Pivot을 중심으로 왼쪽은 작은 수의 정렬, 오른쪽은 큰 수의 정렬
def quick_sort(Arry, start, end):
    if start>=end:
        return
    pivot = start
    left = start+1
    right = end
    
    while (left <= right):
        while (left <= end and Arry[left]<=Arry[pivot]):
            left+=1
        while (start<right and Arry[pivot]<=Arry[right]):
            right-=1
        if (left > right):
            Arry[right], Arry[pivot] = Arry[pivot], Arry[right]
        else:
            Arry[left], Arry[right] = Arry[right], Arry[left]
        
    quick_sort(Arry, start, right-1)
    quick_sort(Arry, right+1, end)
    
if __name__ == "__main__":
    Arry = [9, 8, 1, 3, 2]
    quick_sort(Arry,0,len(Arry)-1)
    print(Arry)