'''
https://www.acmicpc.net/problem/2565

교차하지 않기 위해 제거할 최소한의 전깃줄
'''
import sys

def LIS(arr_Power,num): #오름차순으로 정렬된 것에서 B의 LIS구하기
    dp = [1]*num

    for i in range(1,num):
        for j in range(i):
            if arr_Power[i][1]>arr_Power[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
    # print(arr_Power)
    return (num-max(dp))


def solve():
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  #A,B의 전선 연결 리스트
    arr.sort()  #A기준으로 오름차순 정렬

    print(LIS(arr,N))

if __name__ == "__main__":
    solve()