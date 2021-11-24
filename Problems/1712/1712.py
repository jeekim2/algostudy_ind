#https://www.acmicpc.net/problem/1712
#A 고정비용 B 가변비용, 노트북 비용 C만원

input_val = input()
A = input_val.split()
a = int(A[0])
b = int(A[1])
c = int(A[2])

#expense = a + b*x_input
#profit = c*x_input 2100000000

for x_input in range(2100000000):
    if a + b*x_input < c*x_input:
        print(x_input)
        break
    if x_input == 2100000000:
        print(-1)
        break 