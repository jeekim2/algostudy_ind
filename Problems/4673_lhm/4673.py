#https://www.acmicpc.net/problem/4673

#1~10 self number

#1: 1 + 1 =2
#2 :2 + 2 =4
#3
import math

def DN(i):
    return i + math.floor(i/1000) + math.floor((math.floor(i/100))%10) + math.floor((math.floor(i/10))%10) + math.floor(i%10)


list = []

for i in range(1,10000):
    list.append(DN(i))

for i in range(1,10000):
    if i not in list:
        print(i)
   
    

