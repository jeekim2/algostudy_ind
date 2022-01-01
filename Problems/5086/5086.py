#https://www.acmicpc.net/problem/5086
a, b = map(int, input().split())
while a!=0 and b!=0:
    if b%a ==0 and b/a >1:
        print("factor")
    elif a%b ==0 and a/b >1:
        print("multiple")
    else:
        print("neither")
    a, b = map(int, input().split())