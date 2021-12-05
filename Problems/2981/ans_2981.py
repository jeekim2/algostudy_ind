# https://www.acmicpc.net/problem/2981
import sys


def solve():
    input = sys.stdin.readline

    num_N = int(input())
    N_list = []
    for _ in range(num_N):
        N_list.append(int(input()))

    # N1 = M * x1 + d
    # N2 = M * x2 + d
    # N1 - N2 = M(x1-x2)

    N_list.sort()
    q = N_list[1] - N_list[0]
    for i in range(2, num_N):
        p = N_list[i] - N_list[0]
        # p should be always bigger than q
        while True:
            x = p // q
            d = p % q
            if d == 0:
                break
            p = q
            q = d
    # q 는 모든 차이 값의 최대공약수

    # 최대공약수의 약수 List up
    i = 1
    ans = []
    ans2 = []
    while True:
        i += 1
        if q < i * i:
            break
        if q % i == 0:
            ans.append(i)
            if i != q // i:
                ans2.append(q // i)
    ans2.reverse()
    ans += ans2
    for i in ans:
        print(i, end=" ")
    print(q)


if __name__ == "__main__":
    solve()
