#https://www.acmicpc.net/problem/1541
#최소 값을 구할라면 -가 나오기 전까지는 다 더하다가 - 나오면 그 뒤에꺼 다 괄호로 묶기
a = input().split("-")

#print(a)
sum = 0
for i in a[0].split("+"):
    sum = int(i) + sum

for i in a[1:]:
    for j in i.split("+"):
        sum = sum - int(j)

print(sum)

