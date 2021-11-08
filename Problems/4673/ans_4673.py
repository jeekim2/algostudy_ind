def solve(MAX_NUM):
    dict = {}
    list = []
    for i in range(1, MAX_NUM):
        non_self_num = i
        temp_str = str(i)
        for c in temp_str:
            non_self_num += int(c)
        dict[non_self_num] = 1

    for i in range(1, MAX_NUM):
        if dict.get(i) is None:
            list.append(i)

    for i in list:
        print(i)


if __name__ == "__main__":
    solve(10000)
