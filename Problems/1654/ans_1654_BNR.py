# https://www.acmicpc.net/problem/1654

# 랜선 자르기, 이분 탐색

import sys

def bs(line, N):
    left = 1
    right = max(line)
    while left <= right:
        cnt = 0
        mid = (left+right)//2

        for i in line:
            cnt += i//mid

        if cnt < N: #만들어 낸 개수가 적으면 작게 잘라
            right = mid -1
        else:
            left = mid +1
            ans = mid
    return ans


def solve():
    K, N = map(int, sys.stdin.readline().split()) #K개 가지고 N개 필요함
    K_line = [int(sys.stdin.readline()) for _ in range(K)]

    print(bs(K_line,N))
    

if __name__ == "__main__":
    solve()