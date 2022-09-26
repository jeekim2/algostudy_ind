# https://www.acmicpc.net/problem/15810


def cnt_ballon(Staff, M, time):
    cnt = 0
    for s in Staff:
        cnt += time // s
    if cnt >= M:
        return True
    return False


def solve():
    N, M = map(int, input().split())
    Staff = tuple(map(int, input().split()))
    MinTime = 0
    MaxTime = 1
    while True:
        if cnt_ballon(Staff, M, MaxTime):
            break
        else:
            MinTime = MaxTime
            MaxTime *= 2
    while MaxTime - MinTime > 1:
        midTime = (MinTime + MaxTime) // 2
        if cnt_ballon(Staff, M, midTime):
            MaxTime = midTime
        else:
            MinTime = midTime
    print(MaxTime)
    return


if __name__ == "__main__":
    solve()
