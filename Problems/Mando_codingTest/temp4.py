def solution(numbers):
    answer = 0
    temp =[]
    avg = int((max(numbers)+min(numbers))/2)
    temp_val = 0    

    for i in range(len(numbers)):
            temp.append(numbers[i] -avg)

    for i in range(len(temp)):
        if temp[i] < 0:
            temp[i] = abs(temp[i])

    a= temp.index(min(temp))

    answer = numbers[a]


    return answer


