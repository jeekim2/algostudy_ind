#https://www.acmicpc.net/problem/1152
in_str = str(input())
cnt = 0
i=0
for i in range(len(in_str)):
    if in_str[i] == " ":
        cnt = cnt + 1

if in_str[len(in_str)-1] == " ":
    cnt = cnt - 1

if in_str[0] == " ":
    cnt = cnt - 1    


print(cnt+1)