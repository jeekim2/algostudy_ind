# https://www.acmicpc.net/problem/5904


def solve():
    N = int(input()) - 1
    L = [0, 3]
    while L[-1] <= N:
        L.append(L[-1] * 2 + len(L) + 2)
    while True:
        if N >= L[-2] and N < L[-1] - L[-2]:
            if N == L[-2]:
                print("m")
                return
            print("o")
            return
        if N > L[-2]:
            N -= L[-1] - L[-2]
        L.pop()

    return


if __name__ == "__main__":
    solve()
