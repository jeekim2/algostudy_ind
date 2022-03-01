# https://www.acmicpc.net/problem/2477


def solve():
    Density = int(input())
    Path = []
    for _ in range(6):
        Path.append(list(map(int, input().split())))

    while Path[-1][0] != Path[-3][0] or Path[-2][0] != Path[-4][0]:
        Path.append(Path.pop(0))

    Area = Path[0][1] * Path[1][1] - Path[3][1] * Path[4][1]
    print(Area * Density)
    return


if __name__ == "__main__":
    solve()
