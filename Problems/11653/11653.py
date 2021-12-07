#https://www.acmicpc.net/problem/11653

def Calc(num, list):
    if num > 1:
        list.append(num)
        for i in range(2, num+1):
            if num % i == 0:
                list.append(i)
                list.pop(-2)
                num = num // i
                break
        Calc(num, list)


ans = []
N = int(input())
Calc(N, ans)

for i in range(len(ans)):
    print(ans[i])
