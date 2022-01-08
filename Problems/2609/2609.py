#https://www.acmicpc.net/problem/2609
#유클리드 호제법

a, b = map(int, input().split())

def func1(x,y):
    temp = x % y
    while temp >0:
        x = y
        y = temp
        temp = x % y
    return y    
    
def fucn2(x, y):
    return x * y // func1(x,y)

print(func1(a, b))
print(fucn2(a, b))