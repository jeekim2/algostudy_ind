
# N = int(input())  #재귀 형태 풀이, 시간 초과
# global cnt0
# global cnt1
# cnt0 =0
# cnt1 = 0
# def fibo_up(num):
#     global cnt0
#     global cnt1
#     if num == 0:
#         cnt0 +=1
#         return 0
#     elif num == 1:
#         cnt1 +=1
#         return 1
#     else:
#         return fibo_up(num-1)+fibo_up(num-2)

# fibo(N)
# print(fibo_up(N))
# print(cnt0, cnt1)

memo = []      #메모 형태
TC = []
N = int(input())
for _ in range(N):
    TC.append(int(input()))

def fibo_dp(num):
    for i in range(3,num+1):
        memo.append([memo[i-1][0]+memo[i-2][0], memo[i-1][1]+memo[i-2][1]])
    return memo

for t in TC:
    memo = [[1,0], [0,1], [1,1]] # 0,1,2에 대한 캐시값 저장
    fibo_dp(t)
    print(memo[t][0], memo[t][1])
