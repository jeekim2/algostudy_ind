from typing import no_type_check


def solution(numbers):
    answer = 0
    count = 0
    i_cnt = 0
    for i in numbers:
        count = 0
        i_cnt = i_cnt + 1
        for j in range(len(numbers)-1):
            if i == numbers[j]:
                count = count +1
                
        if count >= int(len(numbers)/2)+1:
            answer = i
        
        if i_cnt == len(numbers) and count <= int(len(numbers)/2)+1:
            answer = -1
        

    return answer

print(solution([6, 1, 6, 6, 7, 5, 6, 7]))