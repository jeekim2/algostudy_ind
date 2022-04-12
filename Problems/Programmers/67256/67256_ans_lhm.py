#https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''


    num = {1:(0,3), 2:(1,3), 3:(2,3), 
            4:(0,2), 5:(1,2), 6:(2,2),
            7:(0,1),8:(1,1),9:(2,1),
            "*":(0,0),0:(1,0),"#":(2,0)}

    left_pos = "*"
    right_pos = "#"

    for i in numbers:

        if i == 1 or i == 4 or i == 7:
            answer+="L"
            left_pos = i

        elif i == 3 or i== 6 or i ==9:
            answer+="R"
            right_pos = i

        elif i == 2 or i ==5 or i==8 or i==0:
            leftdis = abs(num[i][0]-num[left_pos][0])+abs(num[i][1]-num[left_pos][1])
            rightdis = abs(num[i][0]-num[right_pos][0]) + abs(num[i][1]-num[right_pos][1])
            if leftdis == rightdis:
                if hand == "right":
                    answer+="R"
                    right_pos = i
                else:
                    answer+="L"
                    left_pos = i
            elif leftdis > rightdis:
                answer+="R"
                right_pos = i

            else:
                answer+="L"
                left_pos = i


    return answer

