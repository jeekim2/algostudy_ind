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

# (4) 삽입 정렬(Insertion Sort) - 시간초과
#  - 비교 알고리즘 : 이미 정렬된 자료들 + Index의 맞는 위치 찾고 삽입 
#  - 시간복잡도 : O(N^2)              
# def Insertion_Sort():
#     N = int(sys.stdin.readline().strip())
#     Num_list=[]
#     # Index 입력 받기
#     while (len(Num_list)<N):
#         Num_list.append(int(sys.stdin.readline().strip()))
    
#     for i in range(1,len(Num_list)):
#         key = Num_list[i] # key : 삽입할 Index
#         j=i-1 #key의 왼쪽 : i-1까지는 정렬되어 있는 상태
#         while j>=0 and Num_list[j]>key:
#             Num_list[j+1]=Num_list[j]
#             j-=1
#         Num_list[j+1] = key
#     for x in Num_list:
#         print(x)

# (5) 병합 정렬(Merge Sort)
# - 비교 알고리즘 : 분할(배열 크기 = 1까지)+정복(부분 배열 정렬)+합병(새로운 리스트에 복사 후 적용)
# - 시간복잡도 : O(N*logN)
# - 연결리스트로 구성하면 가장 효율적
# def Merge(left, right):
#     result = [] # 새로운 List
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

# def Devide_Merge(Arry):
#     if len(Arry)<=1:
#         return Arry
#     mid = len(Arry)//2
#     leftArea = Arry[:mid]
#     rightArea = Arry[mid:] 
#     leftArea=Devide_Merge(leftArea)
#     rightArea=Devide_Merge(rightArea)
    
#     return Merge(leftArea,rightArea)

# def Merge_Sort():
#     N = int(sys.stdin.readline().strip())
#     Num_list=[]
#     # Index 입력 받기
#     while (len(Num_list)<N):
#         Num_list.append(int(sys.stdin.readline().strip()))
#     result = Devide_Merge(Num_list)
#     for x in result:
#         print(x)

# (6) 퀵 정렬(Quick Sort)
#  - 비교 알고리즘 : 분할(비균등 배열 - under Pivot vs over Pivot)+정복(부분 배열 정렬)+결합
#  - 시간 복잡도 : O(N*logN)
# def Quick_Sort(Arry, start, end): #일반
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
def Quick_Sort(Arry): #Simple Quick
    if len(Arry)<=1:
        return Arry
    pivot, tail = Arry[0], Arry[1:]
    
    left = [x for x in tail if x < pivot]
    right = [y for y in tail if y > pivot]
    
    return Quick_Sort(left)+[pivot]+Quick_Sort(right)

def Merge_Sort():
    N = int(sys.stdin.readline().strip())
    # global Num_list #일반 Quick
    Num_list=[]
    # Index 입력 받기
    while (len(Num_list)<N):
        Num_list.append(int(sys.stdin.readline().strip()))
    #Quick_Sort(Num_list,0,len(Num_list)-1)     #일반 Quick
    Num_list=Quick_Sort(Num_list)
    for x in Num_list:
        print(x)
    
if __name__ == "__main__":
    Merge_Sort()