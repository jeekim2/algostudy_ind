# https://www.acmicpc.net/problem/9663


def checkBoard(row):
    global board
    global N
    # row는 재귀에 따라 증가하며 Queen은 row보다 작은 행에서만 배치되어 있으므로
    # row보다 큰 범위는 확인 할 필요 없음.
    for r in range(row):
        if abs(board[r] - board[row]) == abs(row - r) or board[r] == board[row]:
            return False

    return True


def setQueen(row):
    global board
    global N
    global cnt
    if row == N:
        cnt += 1
        return
    if board[row] == N:
        for col in range(N):
            board[row] = col
            if checkBoard(row):
                setQueen(row + 1)
        board[row] = N


def solve():
    global board
    global N
    global cnt
    N = int(input())
    board = [N] * N
    # index : row / Value : column
    # value가 N 인 경우 아직 Queen이 배치되지 않음.
    cnt = 0
    setQueen(0)
    print(cnt)
    return


if __name__ == "__main__":
    solve()
