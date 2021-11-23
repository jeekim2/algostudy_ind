#  일반 재귀함수로 만들 경우 Time out 되는 경우


def fibo(N):
    global cnt_zero
    global cnt_one
    if N == 0:
        cnt_zero += 1
        return 0
    elif N == 1:
        cnt_one += 1
        return 1
    else:
        return fibo(N - 1) + fibo(N - 2)


def solve():
    global cnt_zero
    global cnt_one
    N = int(input())
    res = []
    for _ in range(N):
        cnt_zero = 0
        cnt_one = 0
        fibo(int(input()))
        res.append([cnt_zero, cnt_one])
    for r in res:
        print(r[0], r[1])


if __name__ == "__main__":
    solve()
