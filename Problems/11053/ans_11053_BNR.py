'''
https://www.acmicpc.net/problem/11053

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열의 길이

LIS (Longest Increasing Subsequence)
https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''
import sys
import bisect

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

def solve1():    #자기 보다 작은 수 dp에 count 업데이트
    dp = [1]*N
    for i in range(1,N):
        for j in range(i):  
            if arr[i]>arr[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)


def solve2():   #자기보다 큰수 dp 업데이트(이진탐색)
    dp = [arr[0]]
    for i in range(1,N):
        if arr[i]>dp[-1]:
            dp.append(arr[i])
        else:
            j = bisect.bisect_left(dp, arr[i])
            dp[j] = arr[i]
        # print(dp)

    return len(dp)

if __name__ == "__main__":
    # print(solve1())
    print(solve2())