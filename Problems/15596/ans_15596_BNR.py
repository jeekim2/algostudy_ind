"""
Name: Bitnuri Kim
Problem: 15596

https://www.acmicpc.net/problem/15596

a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)

리턴값: a에 포함되어 있는 정수 n개의 합 (정수)
"""

a=[] # a= list() 동일

def solve(listA):
    sum= 0
    for i in listA:
        sum = sum + i
    return sum

a = map(int,(input("더할 값 리스트").split())) #spilt(' ')동일
print(solve(a))