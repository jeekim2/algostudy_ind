#https://programmers.co.kr/learn/courses/30/lessons/42583
''' 원래 내가 풀었던 방식
def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossed = [] #다리 지난 트럭
    crossing = [] #다리 건너고 있는 트럭
    crossing_eachcnt = []#다리를 건너고 있는 트럭의 각 시간 count
    waiting = truck_weights #대기 트럭

    timecount = 0
    totalcnt = 0

    end = 0

    while end ==0:
        print("경과시간:",totalcnt)
        print("crossing:",crossing)
        print("each crossing:",crossing_eachcnt)
        print("waiting:",waiting)
        print("crossed:",crossed)
        print("timecount:",timecount)
        print("------------------")
        for i in range(len(crossing)-1):
            crossing_eachcnt[i] = 0


        totalcnt = totalcnt + 1
        if sum(crossing)+ waiting[0] < weight:
            crossing.append(waiting[0])
            waiting.pop(0)
            timecount = timecount +1
            print("1case")
        else:
            timecount = timecount +1
            print("2case")


        if timecount > bridge_length:
            timecount = 0
            crossed.append(crossing[0])
            crossing.pop(0)
        #    crossing.append(waiting)
            print("3case")
        
        if (len(waiting) ==0) and (len(crossing) ==0):
            end = 1
            break



    answer = totalcnt        
    return answer

print(solution(2,10,[7,4,5,6]))
#print(solution(100,100,[10]))
'''
# 풀다가 도저히 어려워서 다른사람 한거 봄
# 다리를 지나가고 있는 차량과 기다리고 있는 차량을 q 라는 변수로 하나로 묶어서 하였음
# bridg_length라는 물리적 거리에 각각 트럭을 올림 ( q = [0]*bridge_length)
# 내가 못푼 이유는 q에 올릴생각을 못함
def solution(bridge_length, weight, truck_weights):
    sec = 0
    q = [0]*bridge_length # [0,0,0,0,...]
    
    while q: 
        sec = sec+1 #시작할때마다 항상 시간 더하기
        q.pop(0) #트럭이 지나갈때마다 하나씩 없어짐
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight: #다리에 있는 트럭의 무게와 대기 중인 트럭의 무게가 제한 무게보다 작거나 같다면
                q.append(truck_weights.pop(0)) #다리에 트럭 올림 
            else:
                q.append(0)#중량 초과만 트럭 안올림
        #print("q:",q)
        #print("sec:",sec)
        #print("------------")

    return sec

#print(solution(2,10,[7,4,5,6]))