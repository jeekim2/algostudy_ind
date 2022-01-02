# https://www.acmicpc.net/problem/1463


def solve():
    N = int(input())
    dic = {}
    dic[1] = 0
    dic[2] = 1
    dic[3] = 1
    if N <= 3:
        print(dic[N])
        return
    for i in range(4, N + 1):
        if i % 3 == 0 and i % 2 == 0:
            tempMin = min(dic[i // 3], dic[i // 2], dic[i - 1])
            dic[i] = tempMin + 1
            continue
        if i % 3 == 0:
            tempMin = min(dic[i // 3], dic[i - 1])
            dic[i] = tempMin + 1
            continue
        if i % 2 == 0:
            tempMin = min(dic[i // 2], dic[i - 1])
            dic[i] = tempMin + 1
            continue
        dic[i] = dic[i - 1] + 1

    print(dic[N])
    return


if __name__ == "__main__":
    solve()
