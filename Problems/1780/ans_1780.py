def CheckAllEqual(row, col, Num):
    defNum = Paper[row][col]
    for i in Paper[row : row + Num]:
        for j in i[col : col + Num]:
            if j != defNum:
                return False
    return True


def CheckDat(row, col, Num, res):
    if Num == 1:
        res[Paper[row][col] + 1] += 1
        return
    else:
        if CheckAllEqual(row, col, Num):
            res[Paper[row][col] + 1] += 1
            return

        for i in range(row, row + Num, Num // 3):
            for j in range(col, col + Num, Num // 3):
                # res = [sum(x) for x in zip(CheckDat(i, j, Num // 3, res), res)]
                CheckDat(i, j, Num // 3, res)


def solve():
    global Paper
    Paper = []
    N = int(input())
    for _ in range(N):
        Paper.append(list(map(int, input().split())))
    res = [0, 0, 0]
    CheckDat(0, 0, N, res)
    for i in res:
        print(i)


if __name__ == "__main__":
    solve()
