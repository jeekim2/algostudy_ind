#https://www.acmicpc.net/problem/1002

#만나는 점 0개
#(x2-x1)^2+(y2-y1)^2 의 루트 값  >  r1+r2
#만나는 점 1개
#(x2-x1)^2+(y2-y1)^2 의 루트 값  =  r1+r2
#만나는 점 2개
#(x2-x1)^2+(y2-y1)^2 의 루트 값  <  r1+r2

T = int(input())
#a =[]
#b =[]

for i in range(T):
    #a = input()
    #b = a.split()
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x2-x1)**2 + (y2-y1)**2)**0.5

    if r == 0 and r1 == r2:
        print(-1)
    elif r == r1+r2:
        print(1)
    elif r == abs(r1-r2):
        print(1)
    elif r > r1 +r2:
        print(0)
    elif r < abs(r1-r2):
        print(0)
    else:
        print(2)