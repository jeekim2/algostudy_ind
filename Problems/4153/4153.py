#https://www.acmicpc.net/problem/4153

while True:
    a,b,c = map(int,input().split())
    A = [a,b,c]
    B = max(A)
    A.remove(B)
    if a == 0 and b == 0 and c == 0:
        break
    if B == int(((A[0])**2+(A[1])**2)**0.5):
        print("right")
    else:
        print("wrong")


