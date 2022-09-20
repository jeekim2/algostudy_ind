# https://www.acmicpc.net/problem/2869


def solve():
    A, B, V = map(int, input().split())
    if A == V:
        print(1)
        return
    if (V - A) % (A - B) > 0:
        print(2 + (V - A) // (A - B))
    else:
        print(1 + (V - A) // (A - B))

    return


if __name__ == "__main__":
    solve()
