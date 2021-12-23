#https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []

    time = 0
    count = 0

    while len(progresses)>0:
        if progresses[0]+speeds[0]*time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count  = count +1

        else:
            time = time +1
            if count > 0:
                answer.append(count)
                count = 0
    answer.append(count)

    return answer