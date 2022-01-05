# https://www.acmicpc.net/problem/2580

import sys


def filtNum(i, j):
    global board
    global defNum
    # 가로줄 확인
    res = defNum - set(board[i])

    # 세로줄 확인
    for v in range(9):
        res = res - {board[v][j]}

    # Block 확인
    for p in range(i // 3 * 3, i // 3 * 3 + 3):
        res = res - set(board[p][j // 3 * 3 : j // 3 * 3 + 3])
    return res


def setNum(i, j):
    global board
    global solveDone
    if solveDone:
        return
    if i == 9:
        for r in board:
            print(" ".join(str(x) for x in r))
        solveDone = True
        return
    if j == 9:
        setNum(i + 1, 0)
        return

    if board[i][j] == 0:
        valNum = filtNum(i, j)
        if valNum:
            for v in valNum:
                board[i][j] = v
                setNum(i, j)
                board[i][j] = 0
        else:
            return
    else:
        setNum(i, j + 1)


def solve():
    global board
    global defNum
    global solveDone
    solveDone = False
    defNum = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    input = sys.stdin.readline
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))
    setNum(0, 0)
    return


if __name__ == "__main__":
    solve()
