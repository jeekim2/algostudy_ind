# https://www.acmicpc.net/problem/10989

import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    # 계수정렬 - Input Range가 통제 가능할 때 사용 가능
    cntArr = [0] * 10001
    for _ in range(N):
        num = int(input())
        cntArr[num] += 1

    # 원래는 count 센 것을 결과에 맞게 재배치해야 하지만
    # print로 바로 뽑아버리므로 불필요
    for num, cnt in enumerate(cntArr):
        for i in range(cnt):
            print(num)


if __name__ == "__main__":
    solve()
