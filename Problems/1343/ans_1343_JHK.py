# https://www.acmicpc.net/problem/1343


def solve():
    s = input()
    i = 0
    res = ""
    for c in s:
        if c == "X":
            i += 1
            if i == 4:
                res += "AAAA"
                i = 0
        else:
            if i == 2:
                res += "BB"
                i = 0
            elif i != 0:
                print(-1)
                return
            res += "."
    if i == 2:
        res += "BB"
    elif i % 2 != 0:
        print(-1)
        return
    print(res)
    return


if __name__ == "__main__":
    solve()
