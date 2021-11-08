def cut_chessboard(chessTable, row, col):
    chessboard = [[0] * 8 for i in range(8)]
    for r in range(8):
        for c in range(8):
            chessboard[r][c] = chessTable[r + row][c + col]
    return chessboard


def diff_chessboard(chessboard, filt):
    cnt = 0

    for r in range(8):
        for c in range(8):
            if chessboard[r][c] == filt[r][c]:
                cnt += 1

    return min(cnt, 64 - cnt)


def solve():
    row_num, col_num = map(int, input().split())
    temp_row = [0] * col_num
    chess_table = [[0] * col_num] * row_num

    for r in range(row_num):
        temp_row_str = list(input())
        for i in range(len(temp_row_str)):
            if temp_row_str[i] == "B":
                temp_row[i] = 1
            else:
                temp_row[i] = 0
        chess_table[r] = temp_row.copy()  # 중요!!!

    chessboard_filt = [[0] * 8 for i in range(8)]
    for r in range(8):
        for c in range(8):
            if (r + c) % 2 == 0:
                chessboard_filt[r][c] = 1
            else:
                chessboard_filt[r][c] = 0

    ans = 64
    for r in range(row_num - 7):
        for c in range(col_num - 7):
            temp_chessboard = cut_chessboard(chess_table, r, c)
            cnt_result = diff_chessboard(temp_chessboard, chessboard_filt)
            if cnt_result < ans:
                ans = cnt_result

    print(ans)


if __name__ == "__main__":
    solve()
