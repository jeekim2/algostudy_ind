def solve():
    series_num = int(input())
    series_cnt = 0
    idx = 665
    while series_num != series_cnt:
        idx += 1
        if str(idx).find("666") >= 0:
            series_cnt += 1

    print(idx)


if __name__ == "__main__":
    solve()
