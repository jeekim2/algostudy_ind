#https://www.acmicpc.net/problem/10818
N = int(input())
print(N)
input_val =[]


for i in range(0,N):
    input_val.append(input())

max = input_val[0]
min = input_val[0]    

for i in range(0,N):
    if int(input_val[i]) > int(max):
        max = input_val[i]
    
    if int(input_val[i]) < int(min):
        min = input_val[i]

print(min, max)