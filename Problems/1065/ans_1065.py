def solve():
    MAX_NUM = int(input())
    ans = 0
    for i in range(1, MAX_NUM + 1):
        num_str = str(i)
        if len(num_str) < 3:
            ans += 1
        else:
            if int(num_str[0]) - int(num_str[1]) == int(num_str[1]) - int(num_str[2]):
                # Only available when the number is below 1000
                ans += 1
    print(ans)


if __name__ == "__main__":
    solve()
