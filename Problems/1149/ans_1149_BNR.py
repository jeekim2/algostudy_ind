'''
https://www.acmicpc.net/problem/1149
'''
# N = int(input())
# global R
# global G
# global B
# R = [0]*N
# G = [0]*N
# B =[0]*N

# for i in range(N):
#     R[i],G[i],B[i] = map(int,input().split())

# def RGB_House(initial):       
#     global R
#     global G    
#     global B
#     cost = 0
#     memo = initial
#     for i in range(1,N):
#         if memo == R[i-1]:
#             cost += memo
#             memo = min(G[i],B[i])

#         elif memo == G[i-1]:
#             cost += memo
#             memo = min(R[i],B[i])

#         elif memo == B[i-1]:
#             cost += memo
#             memo = min(R[i],G[i])
        
#         if i == N-1:
#             cost += memo
#         i += 1
#     return cost

# print(min(RGB_House(R[0]), RGB_House(G[0]), RGB_House(B[0])))



N = int(input())
home = [[0]*3 for i in range(N)]       #2차원 리스트 선언 red,blue,green
cost = [[0]*3 for i in range(N)]

for i in range(N):
    home[i][0], home[i][1], home[i][2] = map(int, input().split())

cost[0][0], cost[0][1], cost[0][2] = home[0][0], home[0][1], home[0][2]     #초기 값(각 색을 선택했을 때의 값)

for i in range(1,N):                                                        #이전 합의 최솟값에 더하는 방식으로 풀어야 함. 각각 현재의 최솟값을 더하면 문제 못품...
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + home[i][0]       
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + home[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + home[i][2]

print(min(cost[-1][0], cost[-1][1], cost[-1][2]))