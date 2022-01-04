#https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#    ans_a = int(a*(int)(10000/len(a)))
#    ans_b = int(b*(int)(10000/len(b)))
#    ans_c = int(c*(int)(10000/len(c)))
    ans_a = a*2000
    ans_b = b*1250
    ans_c = c*1000

    ans_a = ans_a[0:len(answers)]
    ans_b = ans_b[0:len(answers)]
    ans_c = ans_c[0:len(answers)]

    ans_cnt = [0,0,0]

    for i in range(0,len(answers)):
        if ans_a[i] == answers[i]:
            ans_cnt[0] = ans_cnt[0] +1
        if ans_b[i] == answers[i]:
            ans_cnt[1] = ans_cnt[1] +1
        if ans_c[i] == answers[i]:
            ans_cnt[2] = ans_cnt[2] +1

    for i, v in enumerate(ans_cnt):
        if v == max(ans_cnt):
            answer.append(i+1)

    return answer

#print(solution([1,3,2,4,2]))

#enumerate 쓰면 좋음
#for index, value in enumerate(array):
# 이렇게 쓰면 array에 대한 index, value를 그대로 가져다 쓸수 있음
