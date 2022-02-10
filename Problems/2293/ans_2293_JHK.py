# https://www.acmicpc.net/problem/2293

# 이 간단한 점화식을 못구해서 5시간을 삽질함


import sys


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    coin = [int(input().rstrip()) for _ in range(N)]
    # coin = sorted([int(input().rstrip()) for _ in range(N)])

    dic = [0] * (K + 1)
    dic[0] = 1
    # 값이 0인 케이스는 아무것도 선택하지 않는 1개뿐임.

    for c in coin:
        for i in range(c, K + 1):
            dic[i] += dic[i - c]
            # c 동전을 이용해 i 값를 만들 수 있는 방법은 i-c 값을 만드는 갯수와 같다.
    print(dic[-1])
    return


if __name__ == "__main__":
    solve()
