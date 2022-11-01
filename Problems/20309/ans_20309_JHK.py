# https://www.acmicpc.net/problem/20309


def solve():
    N = int(input())
    Nums = list(map(int, input().split()))
    for i, v in enumerate(Nums):
        if i % 2 == v % 2:
            print("NO")
            return
    print("YES")
    return


if __name__ == "__main__":
    solve()
