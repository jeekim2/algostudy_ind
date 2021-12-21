#https://www.acmicpc.net/problem/1110
'''
import math
inputVal = int(input())     #26
#in1 = math.floor(inputVal/10)
in1 = inputVal/10   #2
in2 = inputVal%10               #6
i = 0


input = []
input.insert(0,in1) #2
input.insert(1,in2) #6
input.insert(2,(input[0]+input[1])%10)  #8 
#print(input)    

while True:
    # 26==68?
    if input[0]*10+input[1] != input[i+1]*10+input[i+2]:
        input.insert(i+3,(input[i+1]+input[i+2])%10)
        i = i+1 
       # print(input)  
             
    else:
        print(len(input)-2)  
        break
'''     
a = int(input())
b  = -1
count = 0

while b!=a:
    if b == -1:
        b = a
    b = (b//10 + b%10)%10 + (b%10)*10
    count = count +1

print(count)

