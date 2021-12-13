#https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):

    loc = [i for i in range(len(priorities))] #  priority
    final_loc = [] #정렬 이후 최종 location 값 , 정답

    while len(priorities)!= 0: #정렬 다되면 종료
        if priorities[0] == max(priorities):
            priorities.pop(0)       #조건 만족해서 priorites -> final_loc로 이동
            final_loc.append(loc.pop(0))
        else:
            priorities.append(priorities.pop(0)) #뒤로 옮기기만
            loc.append(loc.pop(0))

    return final_loc.index(location)+ 1

print(solution([2, 1, 3, 2],2))