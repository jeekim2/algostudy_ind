#https://www.acmicpc.net/problem/4344
import sys

C = input() # Num of Test Case :C ex)5 case
Score_Student = []
Max = []
Sum = []
Avg = []
Cnt = []
i,j = 0
#Test case가 1개라고 가정할 경우, i = 0
Max[0] = input() # 3개라고 가정

for j in range(Max[0]):    
    Score_Student[0][j] = input()
    Sum[0] = Sum[0] + Score_Student[0][j]
    if j == Max[0]:
        Avg[0]=Sum[0]/Max[0]

    if Score_Student[0][j] > Avg[0]:
        Cnt[0] = Cnt[0]+1
        
##넘 어렵다 이거..

'''
for i in range(C):    
    Max[i] = input()
    for j in Max[i]:    
        Score_Student[Max[i]][j] = input()
        Sum[i] = Sum[i] + Score_Student[Max[i]][j]
'''