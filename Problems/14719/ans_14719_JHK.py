# https://www.acmicpc.net/problem/14719


def solve():
    H, W = map(int, input().split())
    Polls = list(map(int, input().split()))
    cnt = 0
    for y in range(1, H + 1):
        LeftPoll = 0
        for x in range(W):
            if Polls[x] >= y:
                if LeftPoll > 0:
                    cnt += x - LeftPoll
                LeftPoll = x + 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
