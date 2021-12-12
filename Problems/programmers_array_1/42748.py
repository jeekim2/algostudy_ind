#https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    temp = []
    temp2 =[]

    for start, end, count in commands:
        temp = array[start-1:end]
        temp.sort()
        temp2.append(temp[count-1])
    answer = temp2
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))