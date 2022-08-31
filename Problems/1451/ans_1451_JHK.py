# https://www.acmicpc.net/problem/1451


def get_rect_area(x0, y0, x1, y1, M, N, PSum):
    area = 0
    for y in range(y0, y1 + 1):
        area += PSum[y * M + x1 + 1] - PSum[y * M + x0]
    return area


def get_max_2split(x0, y0, x1, y1, M, N, PSum):
    TempMax = 0
    # split by x (row)
    for y in range(y0, y1):
        Area1 = get_rect_area(x0, y0, x1, y, M, N, PSum)
        Area2 = get_rect_area(x0, y + 1, x1, y1, M, N, PSum)
        TempMax = max(TempMax, Area1 * Area2)
    # split by y (column)
    for x in range(x0, x1):
        Area1 = get_rect_area(x0, y0, x, y1, M, N, PSum)
        Area2 = get_rect_area(x + 1, y0, x1, y1, M, N, PSum)
        TempMax = max(TempMax, Area1 * Area2)

    return TempMax


def solve():
    N, M = map(int, input().split())
    Nums = ""
    for _ in range(N):
        Nums += input()
    PSum = [0]
    Temp = 0
    for c in Nums:
        Temp += int(c)
        PSum.append(Temp)
    # print(get_rect_area(0, 0, 2, 2, M, N, PSum))
    MaxSumMul = 0
    for xidx in range(M):
        for yidx in range(N):
            if xidx == M - 1 and yidx == N - 1:
                break
            FirstArea = get_rect_area(0, 0, xidx, yidx, M, N, PSum)
            if xidx == M - 1:
                MaxSumMul = max(
                    MaxSumMul,
                    FirstArea * get_max_2split(0, yidx + 1, M - 1, N - 1, M, N, PSum),
                )
                continue
            if yidx == N - 1:
                MaxSumMul = max(
                    MaxSumMul,
                    FirstArea * get_max_2split(xidx + 1, 0, M - 1, N - 1, M, N, PSum),
                )
                continue
            secondArea1 = get_rect_area(xidx + 1, 0, M - 1, yidx, M, N, PSum)
            thirdArea1 = get_rect_area(0, yidx + 1, M - 1, N - 1, M, N, PSum)
            secondArea2 = get_rect_area(0, yidx + 1, xidx, N - 1, M, N, PSum)
            thirdArea2 = get_rect_area(xidx + 1, 0, M - 1, N - 1, M, N, PSum)
            if secondArea1 * thirdArea1 > secondArea2 * thirdArea2:
                MaxSumMul = max(secondArea1 * thirdArea1 * FirstArea, MaxSumMul)
            else:
                MaxSumMul = max(secondArea2 * thirdArea2 * FirstArea, MaxSumMul)
            continue
    print(MaxSumMul)
    return


if __name__ == "__main__":
    solve()
