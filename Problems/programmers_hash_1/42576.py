#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
'''
def solution(participant, completion):
    
    answer = 
    return answer
'''
participant = input().split()
completion = input().split()

ans =[]

i = 0 
j = 0
for i in range(len(participant)-1):
    for j in range (len(participant)-1):
        if participant[i] != completion[j]:           
            print("participant:",participant)
            print("completion:",completion)
            print(1)

        else:
            if participant[i]!= " " and completion[j]!= " ":
                participant.remove(participant[i])
                participant.insert(i," ")
                completion.remove(completion[j])
                completion.insert(j," ")
                print("participant:",participant)
                print("completion:",completion)
                print(2)


    i = i +1
print(participant)