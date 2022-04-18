# https://www.acmicpc.net/problem/1300

# 이건 컨닝 좀 함
# N*N 각 행은 각 행의 배수의 나열
# 각 행에서 x보다 작은 수의 갯수 : N//x
# ex. 5행(6의 배수)에서 17보다 작은 수의 갯수 : 17//6 = 2   (6, 12)


def cntLow(N, x):
    cnt = 0
    for i in range(1, N + 1):
        if x > i * N:
            cnt += N
        else:
            cnt += x // i
    return cnt


def solve():
    N = int(input())
    B = int(input())
    left = 0
    right = N * N

    while right - left > 1:
        mid = (left + right) // 2
        valmid = cntLow(N, mid)
        if valmid >= B:
            right = mid
        elif valmid < B:
            left = mid

    print(right)
    return


if __name__ == "__main__":
    solve()
