def solution(arr1,arr2,arr3):
    answer = 0
    temp_arr =[]
    temp2_arr =[]
    for i in arr1:
        for j in arr2:
            if i == j:
                temp_arr.append(i)

    for k in arr3:
        for i in temp_arr:
            if k == j:
                temp2_arr.append(k)

    answer = temp2_arr
    return answer

