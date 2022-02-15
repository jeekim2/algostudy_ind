#https://www.acmicpc.net/problem/1920
# 병합정렬과 이진 탐색 활용하는 풀이 따라하기
def solve():
    N = int(input())
    A_arry = list(map(int, input().split()))
    M = int(input())
    M_arry = list(map(int, input().split()))
    global A_sorted
    A_sorted = merge_sort(A_arry)
    
    for x in M_arry:
        rt = binary_search(0, len(A_sorted), x)
        print(rt)

def merge_sort(Arry):
    if len(Arry) <=1:
        return Arry
    mid = len(Arry)//2
    left = Arry[:mid]
    right = Arry[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    rt = []
    i, j = 0, 0
    while (i < len(left) and j < len(right)):
        if left[i] >= right[j]:
            rt.append(right[j])
            j+=1
        else:
            rt.append(left[i])
            i+=1
    while (i < len(left)):
        rt.append(left[i])
        i+=1
    while (j < len(right)):
        rt.append(right[j])
        j+=1
        
    return rt
        
def binary_search(left, right, target):
    while(left < right):
        mid = (left+right)//2
        if A_sorted[mid] < target:
            left = mid+1
        else:
            if A_sorted[mid] == target:
                return 1
            else:
                right = mid
    return 0
    
if __name__ == "__main__":
    solve()
    