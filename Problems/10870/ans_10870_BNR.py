#https://www.acmicpc.net/problem/10870

Num = int(input())

n = 2
array = [0, 1]

def Fibo(n, array):
    if n <= Num:
        array.append(array[n-2] + array[n-1]) 
        return Fibo(n+1, array)
    else:
        return array

if Num < 2:
    print(Num)
else:
    Fibo(n,array)
    print(array[Num])