# https://www.acmicpc.net/problem/9527


def solve():
    A, B = map(int, input().split())
    OneCnt = [0, 1]
    i = 2
    j = 0
    k = 1
    while i <= B:
        if i == 2**k:
            j = 0
            k += 1
        OneCnt.append(OneCnt[j] + 1)
        j += 1
        i += 1
    print(sum(OneCnt[A:]))
    return


def cnt_bin(num, dp):
    if num in dp:
        return dp[num]
    if num == 0:
        return 0
    if num == 1:
        return 1
    i = 1
    while i * 2 <= num:
        i *= 2
    dp[num] = cnt_bin(i - 1, dp) + cnt_bin(num - i, dp) + num - i + 1
    return dp[num]


def solve2():
    A, B = map(int, input().split())
    dp = {}
    print(cnt_bin(B, dp) - cnt_bin(A - 1, dp))
    return


if __name__ == "__main__":
    solve2()
