#https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    zerocnt = 0
    matchcnt = 0
    #0갯수 확인
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zerocnt +=1
    #매치 갯수 확인
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                matchcnt +=1

    
    mincnt = matchcnt
    maxcnt = matchcnt + zerocnt

    #순위 정하기
    if maxcnt == 6:
        maxans = 1
    elif maxcnt == 5:
        maxans = 2
    elif maxcnt == 4:
        maxans = 3
    elif maxcnt == 3:
        maxans = 4
    elif maxcnt == 2:
        maxans = 5
    else:
        maxans = 6

    if mincnt == 6:
        minans = 1
    elif mincnt == 5:
        minans = 2
    elif mincnt == 4:
        minans = 3
    elif mincnt == 3:
        minans = 4
    elif mincnt == 2:
        minans = 5
    else:
        minans = 6

    answer = maxans,minans
    return answer