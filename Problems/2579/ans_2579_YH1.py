#https://www.acmicpc.net/problem/2579
import sys
# 재귀호출 시도해봤으나.. 경우의 수가 아닌 합계를 구하는 거라 적용이 안됨.
# 계단별 True/False + 계단별 점수 확인 + 합산 식으로 고려했으나 너무 복잡
# 리뷰 후에 풀어서인지 같은 방식만 생각나서 일단 풀게 됨....
def solve():
    input = sys.stdin.readline
    N = int(input())
    stair = []
    for _ in range(N):
        stair.append(int(input()))
    StairScore(stair)

def StairScore(stair):
    maxS = [0]*len(stair)
    for i in range(len(stair)):
        if i == 0 :
            maxS[i] = [stair[0], 0]
        elif i == 1 :
            maxS[i] = [stair[0]+stair[1], stair[1]]
        else:
            maxS[i] = [stair[i]+maxS[i-1][1], stair[i]+max(maxS[i-2])]
    print(max(maxS[-1]))    

if __name__ == "__main__":
    solve()