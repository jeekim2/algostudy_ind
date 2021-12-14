# https://www.acmicpc.net/problem/2751 풀이에서 Seminar로 전환
# Seminar - 정렬
import sys
from timeit import *

num_list = [9, 3, 7, 2, 1, 5, 6, 4, 8]

# (1) 순차 정렬(Sequential sort) - 시간 초과
# - 비교 알고리즘 : 현재 Index vs 뒤의 나머지 비교 후 교환(0~N까지 순차)
# - 시간복잡도 : O(N^2), 비교 횟수 가장 많음.
def Sequential_Sort(num_list):
    #0~N까지 순차적으로 진행 및 정렬
    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    # print(num_list)

# (2) 선택 정렬(Selection sort) - 시간초과
#  - 비교 알고리즘 : 이미 정해진 위치 + 그 위치에 넣을 Index 선택(최솟값)
#  - 시간복잡도 : O(N^2) 
def Selection_Sort(Num_list) :
    for i in range(len(Num_list)-1):
        minIndex = i # 배치될 위치
        for j in range(i+1, len(Num_list)):
            if Num_list[j]<Num_list[minIndex]: # 최솟값 찾기
                minIndex = j
        Num_list[i], Num_list[minIndex] = Num_list[minIndex], Num_list[i]
    # print(Num_list)

# (3) 버블 정렬(Bubble Sort) - 시간초과
# - 비교 알고리즘 : 인접한 두 Index 비교 및 교환 - 끝에서부터 정렬
# - 시간복잡도 : O(N^2)
def Bubble_Sort(Num_list):
    for i in range(1, len(Num_list)):
        for j in range(len(Num_list)-i):
            if Num_list[j] > Num_list[j+1]:
                Num_list[j], Num_list[j+1] = Num_list[j+1], Num_list[j]
    # print(Num_list)

# (4) 삽입 정렬(Insertion Sort) - 시간초과
#  - 비교 알고리즘 : 이미 정렬된 자료들 + Index의 맞는 위치 찾고 삽입 
#  - 시간복잡도 : O(N^2)              
def Insertion_Sort(Num_list):
    for i in range(1,len(Num_list)):
        key = Num_list[i] # key : 삽입할 Index
        j=i-1 #key의 왼쪽 : i-1까지는 정렬되어 있는 상태
        while j>=0 and Num_list[j]>key:
            Num_list[j+1]=Num_list[j]
            j-=1
        Num_list[j+1] = key
    # print(Num_list)

# (5) 병합 정렬(Merge Sort)
# - 비교 알고리즘 : 분할(배열 크기 = 1까지)+정복(부분 배열 정렬)+합병(새로운 리스트에 복사 후 적용)
# - 시간복잡도 : O(N*logN)
# - 연결리스트로 구성하면 가장 효율적
def Merge(left, right):
    result = [] # 새로운 List
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left)>0:
            result.append(left[0])
            left = left[1:]
        elif len(right)>0:
            result.append(right[0])
            right = right[1:]
        else:
            pass
    return result

def Devide_Merge(Arry):
    if len(Arry)<=1:
        return Arry
    mid = len(Arry)//2
    leftArea = Arry[:mid]
    rightArea = Arry[mid:] 
    leftArea=Devide_Merge(leftArea)
    rightArea=Devide_Merge(rightArea)
    
    return Merge(leftArea,rightArea)

def Merge_Sort(Num_list):
    result = Devide_Merge(Num_list)
    # print(result)

# (6) 퀵 정렬(Quick Sort)
#  - 비교 알고리즘 : 분할(비균등 배열 - under Pivot vs over Pivot)+정복(부분 배열 정렬)+결합
#  - 시간 복잡도 : O(N*logN)
# def Quick_Sort(Arry, start, end): # Python 언어 특성 상관없는 일반적인 구현
#     if start>=end:
#         return
#     pivot = start
#     low = start+1
#     high = end
    
#     while (low <= high):
#         while (low <= end and Arry[low]<=Arry[pivot]):
#             low+=1
#         while (start<high and Arry[pivot]<=Arry[high]):
#             high-=1
#         if (low > high):
#             Arry[high], Arry[pivot] = Arry[pivot], Arry[high]
#         else:
#             Arry[low], Arry[high] = Arry[high], Arry[low]
        
#     Quick_Sort(Arry, start, high-1)
#     Quick_Sort(Arry, high+1, end)
    
def Quick_Sort(Arry): # Python 언어 특성에 맞는 Simple한 구현
    if len(Arry)<=1:
        return Arry
    pivot, tail = Arry[0], Arry[1:]
    
    left = [x for x in tail if x < pivot]
    right = [y for y in tail if y > pivot]
    
    return Quick_Sort(left)+[pivot]+Quick_Sort(right)

def Merge_Quick_Sort(Num_list):
    #Quick_Sort(Num_list,0,len(Num_list)-1)     #일반 Quick
    Num_list=Quick_Sort(Num_list)
    # print(Num_list)

# 실행시간 비교
t1 = Timer("Sequential_Sort([9, 3, 7, 2, 1, 5, 6, 4, 8])", "from __main__ import Sequential_Sort")
t2 = Timer("Selection_Sort([9, 3, 7, 2, 1, 5, 6, 4, 8])", "from __main__ import Selection_Sort")
t3 = Timer("Bubble_Sort([9, 3, 7, 2, 1, 5, 6, 4, 8])", "from __main__ import Bubble_Sort")
t4 = Timer("Insertion_Sort([9, 3, 7, 2, 1, 5, 6, 4, 8])", "from __main__ import Insertion_Sort")
t5 = Timer("Merge_Sort([9, 3, 7, 2, 1, 5, 6, 4, 8])", "from __main__ import Merge_Sort")
t6 = Timer("Merge_Quick_Sort([9, 3, 7, 2, 1, 5, 6, 4, 8])", "from __main__ import Merge_Quick_Sort")
print("Sequential_Sort", "%0.8f"%t1.timeit(number=1), "seconds")
print("Selection_Sort", "%0.8f"%t2.timeit(number=1), "seconds")
print("Bubble_Sort", "%0.8f"%t3.timeit(number=1), "seconds")
print("Insertion_Sort", "%0.8f"%t4.timeit(number=1), "seconds")
print("Merge_Sort", "%0.8f"%t5.timeit(number=1), "seconds")
print("Merge_Quick_Sort", "%0.8f"%t6.timeit(number=1), "seconds")
