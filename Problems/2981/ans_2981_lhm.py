#https://www.acmicpc.net/problem/2981
'''
T = int(input())
a = []
ans =[]
for i in range(T):
    a.append(int(input()))

#print(a)

for j in range(2, min(a)):
    for i in range(1,T):
        if a[0]%j != a[i]%j:
            break
        else:
            if i == T-1:
                ans.append(j)


print(*ans)
'''

#나머지가 같은 수를 찾는 것은 서로 다른 수의 차의 약수와 같음
#두 값들의 차이에서 최대 공약수를 구하고 이어 약수를 구하기
#최대 공약수 구하기
def gcd(x,y):   #유틀리드 호제법
    if x < y:
        x,y = y,x
    r = x%y
    while r >0:
        x= y
        y= r
        r = x%y
    return y
#약수 구하기
def div(x):
    divlist = [x] # 원래 값 넣음
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            divlist.append(i)
            if x//i != i:
                divlist.append(x//i)
    divlist.sort()
    return divlist

T = int(input())
a = []
ans =[]
for i in range(T):
    a.append(int(input()))
a.sort(reverse=True) # 들어오는 숫자를 뺏을 때 양수 만들기 위함

a_diff = []
for i in range(len(a)-1):
    a_diff.append(a[i]-a[i+1])

if a_diff ==1:
    ans = a_diff[0]
elif a_diff ==2:
    ans = gcd(a_diff[0], a_diff[1])
else:
    ans = a_diff[0]
    for i in range(1, len(a_diff)):
        ans = gcd(a_diff[i], ans)

print(*(div(ans)))