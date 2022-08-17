# https://www.acmicpc.net/problem/9997
import sys


def Explore_Word(i, N, AlphaWords, AlphaCheck):
    AlphaCheck |= AlphaWords[i]
    if AlphaCheck == (1 << 26) - 1:
        return 1 << (N - i - 1)
    else:
        res = 0
        j = i + 1
        while j < N:
            temp = Explore_Word(j, N, AlphaWords, AlphaCheck)
            res += temp
            j += 1
        return res


def word_bit(w):
    res = 0
    for c in w:
        res |= 1 << (ord(c) - ord("a"))
    return res


def solve():
    input = sys.stdin.readline
    N = int(input())
    AlphaWords = [0] * N
    for i in range(N):
        AlphaWords[i] = word_bit(input().rstrip())
    cnt = 0
    i = 0
    while i < N:
        temp = Explore_Word(i, N, AlphaWords, 0)
        cnt += temp
        i += 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
