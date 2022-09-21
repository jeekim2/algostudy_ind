# https://www.acmicpc.net/problem/1057


def solve():
    N, A, B = map(int, input().split())
    cnt = 1
    N -= 1
    A -= 1
    B -= 1
    if A > B:
        A, B = B, A
    while True:
        if A % 2 == 0 and A + 1 == B:
            print(cnt)
            return
        A //= 2
        B //= 2
        cnt += 1
    return


if __name__ == "__main__":
    solve()
