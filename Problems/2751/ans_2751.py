#https://www.acmicpc.net/problem/2751

import sys
# Seminar - 정렬
# (1) 순차 정렬(Sequential sort) - 시간 초과
# - 비교 알고리즘 : 현재 Index vs 뒤의 나머지 비교 후 교환(0~N까지 순차)
# - 시간복잡도 : O(N^2), 비교 횟수 가장 많음.
# def Sequential_Sort():
#     N = int(sys.stdin.readline().strip())
#     num_list=[]
#     # Index 입력 받기 
#     while len(num_list)< N:      
#         num_list.append(int(sys.stdin.readline().strip()))
#     #0~N까지 순차적으로 진행 및 정렬
#     for i in range(len(num_list)-1):
#         for j in range(i+1, len(num_list)):
#             if num_list[i] > num_list[j]:
#                 num_list[i], num_list[j] = num_list[j], num_list[i]
#     for x in num_list : 
#         print(x)

# (2) 선택 정렬(Selection sort) - 시간초과
#  - 비교 알고리즘 : 이미 정해진 위치 + 그 위치에 넣을 Index 선택(최솟값)
#  - 시간복잡도 : O(N^2) 
# def Selection_Sort() :
#     N = int(sys.stdin.readline().strip())
#     Num_list=[]
#     # Index 입력 받기
#     while len(Num_list)<N:
#         Num_list.append(int(sys.stdin.readline().strip()))
    
#     for i in range(len(Num_list)-1):
#         minIndex = i # 배치될 위치
#         for j in range(i+1, len(Num_list)):
#             if Num_list[j]<Num_list[minIndex]: # 최솟값 찾기
#                 minIndex = j
#         Num_list[i], Num_list[minIndex] = Num_list[minIndex], Num_list[i]
#     for x in Num_list:
#         print(x)

# (3) 버블 정렬(Bubble Sort) - 시간초과
# - 비교 알고리즘 : 인접한 두 Index 비교 및 교환 - 끝에서부터 정렬
# - 시간복잡도 : O(N^2)
# def Bubble_Sort():
#     N = int(sys.stdin.readline().strip())
#     Num_list=[]
#     # Index 입력 받기
#     while len(Num_list)<N:
#         Num_list.append(int(sys.stdin.readline().strip()))
        
#     for i in range(1, len(Num_list)):
#         for j in range(len(Num_list)-i):
#             if Num_list[j] > Num_list[j+1]:
#                 Num_list[j], Num_list[j+1] = Num_list[j+1], Num_list[j]
#     for x in Num_list:
#         print(x)

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
# def quick_sort(Arry, start, end):
#     if start>=end:
#         return
#     pivot = start
#     left = start+1
#     right = end
    
#     while (left <= right):
#         while (left <= end and Arry[left]<=Arry[pivot]):
#             left+=1
#         while (start<right and Arry[pivot]<=Arry[right]):
#             right-=1
#         if (left > right):
#             Arry[right], Arry[pivot] = Arry[pivot], Arry[right]
#         else:
#             Arry[left], Arry[right] = Arry[right], Arry[left]
        
#     quick_sort(Arry, start, right-1)
#     quick_sort(Arry, right+1, end)
    
# if __name__ == "__main__":
#     Arry = [9, 8, 1, 3, 2]
#     quick_sort(Arry,0,len(Arry)-1)
#     print(Arry)
if __name__ == "__main__":
    Bubble_Sort()