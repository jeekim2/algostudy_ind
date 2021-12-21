# import math


def is_prime_num(n,m):
    arr = [True] * (m - n + 1) #소수가 삭제되었는지 확인하는 배열 선언
    
    f=0
    j = n
    if j==1:
        arr[f] = True
        f = 1
        j = n +1
    while j <= m//2:
        i = 2
        while i <= m//2:
            if j%i != 0:
                arr[f] = False
                j = j+1
                break
            if i == m//2:
                print(arr[f])
            j = j+1
    return arr

arr = is_prime_num(1, 5)
print(arr)
for i in range(1, 5):
    if arr[i] == True:
        print(i, end=' ')