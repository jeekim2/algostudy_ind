#https://www.acmicpc.net/problem/2309


P = []
array = []
copyarray = []
result = []
for _ in range(9):
    P.append(int(input()))

def find():
    for i in range(len(P)):
        array = P.copy()
        array[i]=0
        for j in range(i+1,len(P)):
            copyarray = array.copy()
            # print(copyarray)
            copyarray[j]=0
            if sum(copyarray) == 100:
                # print(copyarray)
                return copyarray
arr = find()
arr.sort()
for i in arr[2:]:
    print(i)


