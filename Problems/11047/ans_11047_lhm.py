#https://www.acmicpc.net/problem/11047
import  sys
input = sys.stdin.readline
N, K = map(int,input().split())

coin = [0]*N
ans = 0

for i in range(N):
    coin[i] = int(input())

#지금 아래꺼 시간초과
'''
while coin:
    if coin[-1] <= K:
        ans = ans+1
        K = K - coin[-1]
    else:
        coin.pop(-1)
    #print("coin[-1]:",coin[-1])
    #print("coin[]",coin)
    #print("ans",ans)
    #print("K",K)
    #print("---------")
'''

for i in range(1,N+1):
    temp = coin[-i]
    if K >=temp:
        temp2 = K//temp
        K = K - temp2*temp
        ans = ans + temp2
        #print("temp2:",temp2)
        #print("temp:",temp)
        #print("K:",K)
        #print("-----------")

print(ans)