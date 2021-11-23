def save_pattern(N):
    if N > 3:
        N /= 3
        temp_pat = save_pattern(N)
        blank_pat = [str(i).replace("*", " ") for i in temp_pat]
        lenPat = len(temp_pat) * 3
        pat = [""] * lenPat
        for i in range(lenPat):
            p = int(i % N)
            if i >= lenPat / 3 and i < lenPat / 3 * 2:
                pat[i] = temp_pat[p] + blank_pat[p] + temp_pat[p]
            else:
                pat[i] = temp_pat[p] * 3
    else:
        pat = ["***", "* *", "***"]

    return pat


def solve():
    N = int(input())
    pat = save_pattern(N)
    for i in pat:
        print(i)
    return 0


if __name__ == "__main__":
    solve()
