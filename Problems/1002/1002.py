#https://www.acmicpc.net/problem/1002

#만나는 점 0개
#(x2-x1)^2+(y2-y1)^2 의 루트 값  >  r1+r2
#만나는 점 1개
#(x2-x1)^2+(y2-y1)^2 의 루트 값  =  r1+r2
#만나는 점 2개
#(x2-x1)^2+(y2-y1)^2 의 루트 값  <  r1+r2

T = int(input())
a =[]
b =[]

for i in range(T):
    a = input()
    b = a.split()
    if i == T:
        break
    if (int(b[3])==int(b[0]))and (int(b[4])==int(b[1])):
        if int(b[2])==int(b[5]):
            print(-1)
        else:
            print(0)
    else:
        a0 = {((int(b[3])-int(b[0]))**2 + (int(b[4])-int(b[1]))**2)**0.5, int(b[2]),int(b[5])}
        a1 = max(((int(b[3])-int(b[0]))**2 + (int(b[4])-int(b[1]))**2)**0.5, int(b[2]),int(b[5]))
        a2 = a0.remove(a1)

        if int(a1) > int(sum((a0))):
            print(0)

        elif int(a1) == int(sum((a0))):
            print(1)

        else:
            print(2)

