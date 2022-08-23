# https://www.acmicpc.net/problem/2473


def solve():
    N = int(input())
    Sols = sorted(list(map(int, input().split())))
    MinSolSum = 3000000001
    for i in range(N - 1):
        j, k = i + 1, N - 1
        while j < k:
            res = Sols[i] + Sols[j] + Sols[k]
            if res == 0:
                print(Sols[i], Sols[j], Sols[k])
                return
            if abs(res) < MinSolSum:
                MinSolSum = abs(res)
                ans = [Sols[i], Sols[j], Sols[k]]
            if res < 0:
                j += 1
            else:
                k -= 1
    print(*ans)
    return


if __name__ == "__main__":
    solve()
