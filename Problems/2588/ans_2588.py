A=int(input())
B=input()
C=B[::-1]

for i in range(len(C)):
    print(A*int(C[i]))
    
print(A*int(B))