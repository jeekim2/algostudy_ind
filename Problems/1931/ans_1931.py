import sys


def solve():
    input = sys.stdin.readline
    # 그냥 input 함수보다 sys.stdin.readline이 빠름. Function override 사용
    N = int(input())
    req = []
    for _ in range(N):
        s, e = map(int, input().split())
        req.append((e, s))
    # req.sort(key=lambda x: x[1])
    req.sort()  # 이 정렬 방법은 기억하자
    # 종료시간 우선 정렬, 같은 경우 시작 시간순 정렬
    endTime = 0
    cnt = 0

    for r in req:
        if r[1] >= endTime:
            endTime = r[0]
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    solve()
