import math

input1 = int(input())
input2 = int(input())

ans1 = input1*(input2%10)
ans2 = input1*(math.floor((input2%100)/10))
ans3 = input1*(math.floor(input2/100))
ans4 = ans3*100+ans2*10+ans1
print(ans1)
print(ans2)
print(ans3)
print(ans4)

