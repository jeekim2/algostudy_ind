# https://www.acmicpc.net/problem/1992

import sys


def quad(ulx, uly, drx, dry):
    global dat
    all_same = True
    init_dat = dat[uly][ulx]
    for row in dat[uly : dry + 1]:
        for d in row[ulx : drx + 1]:
            if init_dat != d:
                all_same = False
    if all_same == True:
        return str(init_dat)

    ans = "("
    ans += quad(ulx, uly, (ulx + drx) // 2, (uly + dry) // 2)  # up left
    ans += quad((ulx + drx) // 2 + 1, uly, drx, (uly + dry) // 2)  # up right
    ans += quad(ulx, (uly + dry) // 2 + 1, (ulx + drx) // 2, dry)  # down left
    ans += quad((ulx + drx) // 2 + 1, (uly + dry) // 2 + 1, drx, dry)  # down right
    ans += ")"
    return ans


def solve():
    global dat
    input = sys.stdin.readline
    N = int(input())
    dat = []
    for _ in range(N):
        dat.append(list(map(int, list(input().rstrip()))))

    ans = quad(0, 0, N - 1, N - 1)
    print(ans)


if __name__ == "__main__":
    solve()
