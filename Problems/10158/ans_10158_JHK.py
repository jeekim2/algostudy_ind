# https://www.acmicpc.net/problem/10158


def move(Pos, Limit, Time):
    Time %= Limit * 2
    # 왕복하면 제자리이므로 미리 제거
    Dir = True
    while Time > 0:
        if Dir:
            Pos += 1
            if Pos == Limit:
                Dir = False
        else:
            Pos -= 1
            if Pos == 0:
                Dir = True
        Time -= 1
    return Pos


def solve():
    W, H = map(int, input().split())
    P, Q = map(int, input().split())
    T = int(input())
    print(move(P, W, T), end=" ")
    print(move(Q, H, T))
    return


if __name__ == "__main__":
    solve()
