import math
inputVal = int(input())
in1 = math.floor(inputVal/10)   
in2 = inputVal%10               
i = 0
print(in1,in2)

input = []
input.insert(0,in1)
input.insert(1,in2)
    

for i in range(1000):
    input.insert([i+2],(input[i]+input[i+1])%10) 
    i = i+1

    if input[i]*10+input[i+1] == input[i+1]*10+input[i+2]:
        break             
        

print(i)
