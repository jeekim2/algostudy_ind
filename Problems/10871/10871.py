"""
Name: Bitnuri Kim
Problem: 10871

https://www.acmicpc.net/problem/10871

첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
"""


N, X = map(int, input("N개 X정수 입력").split(' '))
A = list(map(int, input("수열 N개 만큼 입력").split(' ')))
B = list()

idx=0
for i in A:
    if i < X:
        B.append(i)
    idx = idx +1

strB = " ".join(map(str,B)) #join은 str type만 가능
print(strB)