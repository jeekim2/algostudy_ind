# https://www.acmicpc.net/problem/15651

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

import sys


def search(depth):
    global N
    global M
    global arr
    if depth >= M:
        print(" ".join(str(x) for x in arr))
        return
    for i in range(N):
        i += 1
        # 좋아보이는 코드는 아닌데, for i in range(1,N+1) 보다 갑자기 이뻐보임
        arr[depth] = i
        search(depth + 1)
    return


def solve():
    global N
    global M
    global arr
    input = sys.stdin.readline
    N, M = map(int, input().split())
    # 단순히 생각하면, 1~N 까지 반복문을 M번 중첩하면 되지만...
    arr = [0] * M
    search(0)
    return


if __name__ == "__main__":
    solve()
