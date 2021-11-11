def solve():
    N = int(input())
    ggg = []
    for _ in range(N):
        ggg.append(input().split())
    for g in ggg:
        for s in g[1]:
            for _ in range(int(g[0])):
                print(s, end="")
        print()


if __name__ == "__main__":
    solve()
