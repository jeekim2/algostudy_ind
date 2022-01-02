#https://programmers.co.kr/learn/courses/30/lessons/42584
# 내가 제출한 답, 정확성은 맞았으나 효율성에서 실패 함
'''
def solution(prices):
    answer = []
    cnt = 0
    temp = prices[1:len(prices)]
    while prices:

        cnt = cnt +1    
        if len(prices)==1:  #price 마지막 한개 남으면 비교할 대상이 없기때문에 그냥 exit
            answer.append(0)
            break

        if prices[0] <= temp[0]:                       
            temp.pop(0)
        else:
            answer.append(cnt)
            cnt = 0      
            prices.pop(0)
            temp = prices[1:len(prices)]
        
        if len(temp)==0:
            answer.append(cnt)
            cnt = 0
            prices.pop(0)
            temp = prices[1:len(prices)]     

    return answer
'''

#다른 사람 풀이/ 다른 사람 풀이 이긴 한데 구조가 간단하고 해서 같은 구조를 외워서 다른 문제 사용 가능할듯 합니다.


def solution(prices):
    result =[0]*len(prices) # 우선 가격에 대해 0으로 모두 채워 넣는다
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] <= prices [j]:
                result[i] = result[i]+1
            else:
                break
    return result