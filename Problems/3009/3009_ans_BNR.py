#https://www.acmicpc.net/problem/3009

x = []
y = []
for i in range(3):
    A, B = list(map(int, input().split()))

    if A in x:
        x.remove(A)
    else:
        x.append(A)
    if B in y:
        y.remove(B)
    else:
        y.append(B)
print(x[0], y[0])
    