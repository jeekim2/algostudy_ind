def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossed = [] #다리 지난 트럭
    #truck_weights 대기 트럭
    waiting = [] #다리 건너고 있는 트럭
    timecount = 0

    for i in range(bridge_length):
        if sum(waiting) <= weight:
            waiting.append(truck_weights[i])
            timecount = timecount +1


    return answer