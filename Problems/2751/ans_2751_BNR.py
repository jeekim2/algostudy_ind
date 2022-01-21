# https://www.acmicpc.net/problem/2751


N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

# def quicksolve(arr):
#     if len(arr)<=1:
#         return arr
#     pivot = arr[-1]
#     tail = arr[:-1]
#     less = []
#     more = []
#     # equal = []

#     for i in tail:
#         if i < pivot:
#             less.append(i)
#         elif i > pivot:
#             more.append(i)

#     return quicksolve(less) + [pivot] + quicksolve(more)
# print(quicksolve(array))

def merge(le, ri):
    i = 0
    j = 0
    sorted_list = []

    while(i<len(le)) and (j<len(ri)): #비교해서넣기
        if le[i]<ri[j]:
            sorted_list.append(le[i])
            i+=1
        else:
            sorted_list.append(ri[j])
            j+=1
    while (i<len(le)):              #남은 값 넣기
        sorted_list.append(le[i])
        i+=1
    while (j<len(ri)):
        sorted_list.append(ri[j])
        j+=1
    return sorted_list

def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)

    return merge(left1, right1)     #나누고 merge call

result = merge_sort(array)

for i in result:
    print(i)