def findTime(leng):
    i = 0
    while True:
        i0_sq = i * i
        i1_sq = (i + 1) * (i + 1)
        if leng > i0_sq and leng <= i1_sq:
            if leng <= i * (i + 1):
                ans = 2 * i
            else:
                ans = 2 * i + 1
            break
        i += 1
    return ans


def solve():
    TC_NUM = int(input())
    TCs = []
    for _ in range(TC_NUM):
        TC = input().split()
        TCs.append(int(TC[1]) - int(TC[0]))

    for i in TCs:
        print(findTime(i))


if __name__ == "__main__":
    solve()

# Result : 1 1 2 2 3 3 4 4 5 5 ...
# 1  1
# 2  1 1
# 3  1 1 1
# 4  1 2 1
# 5  1 2 1 1
# 6  1 2 2 1
# 7  1 2 2 1 1
# 8  1 2 2 2 1
# 9  1 2 3 2 1
# 10 1 2 3 2 1 1
# 11 1 2 3 2 2 1
# 12 1 2 3 3 2 1
# 13 1 2 3 3 2 1 1
# 14 1 2 3 3 2 2 1
# 15 1 2 3 3 3 2 1
# 16 1 2 3 4 3 2 1
# 17 1 2 3 4 3 2 1 1
# 18 1 2 3 4 3 2 2 1
# 19 1 2 3 4 3 3 2 1
# 20 1 2 3 4 4 3 2 1
# 21 1 2 3 4 4 3 2 1 1
# 22 1 2 3 4 4 3 2 2 1
# 23 1 2 3 4 4 3 3 2 1
# 24 1 2 3 4 4 4 3 2 1
# 25 1 2 3 4 5 4 3 2 1
# 26 1 2 3 4 5 4 3 2 1 1
